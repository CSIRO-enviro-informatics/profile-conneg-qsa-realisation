import os
from flask import Flask, Blueprint, render_template, request, Response
import json
import metadata

APP_DIR = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)

'''
REFS:
    Memento spec: https://tools.ietf.org/rfc/rfc7089
'''

# TODO: support CURIE advertising & compare to OAI-PMH
'''One option is to use CURIE syntax prefix:token in which case this would be sematically equivalent to the full URI 
form. This would require the server implementation to be willing to advertise prefixes it understands, or clients to 
specify prefix assumptions and to match either full URI or CURIE forms.'''

# TODO: register of registers


@app.route('/')
def home():
    # TODO: add about info here
    # TODO: add implemented instance info here
    return render_template('home.html', BASE_URI=metadata.BASE_URI)


class QueryStringArgumentError(Exception):
    def __init__(self):
        super().__init__('Query String Arguments must have the keys _profile or _mediatype.')


def validate_qsas():
    for key, value in request.values.items():
        if key not in ['_profile', '_mediatype']:
            raise QueryStringArgumentError()


@app.route('/catalogue')
@app.route('/paper/<string:id>')
@app.route('/license/<string:id>')
def resource(id=None):
    '''
    1. Validate input

    2. Make Link headers

    3. Handle list requests

    4. Handle list-token requests
    '''
    # 1. Validate input
    try:
        validate_qsas()
    except QueryStringArgumentError as e:
        return Response(str(e), status=400, mimetype='text/plain')

    # 2. Make Link headers
    # regardless of the method/QSA, get the profiles for Link headers
    profiles = metadata.list_profiles_for_resource(request.base_url, return_only_uris=True)
    headers = {}
    if profiles[0] is not None:
        links = ''
        for profile in profiles:
            links += '<{}>; rel="dct:conformsTo",'.format(profile)
        links = links[:-1]
        headers['Link'] = links

    # 3. Handle list requests
    if request.values.get('_profile') == 'list':
        # this request can only adhere to shich profile
        headers = {'Content-Profile': '{}'.format('http://www.w3.org/ns/prof/')}  # TODO: address this meta profile
        # either return a text/uri-list, application/json or text/html
        if request.accept_mimetypes.best_match(['application/json', 'text/uri-list', 'text/html']) == 'text/uri-list' \
                or request.values.get('_mediatype') == 'text/uri-list':
            return Response('\n'.join(profiles), mimetype='text/uri-list', headers=headers)
        elif request.accept_mimetypes.best_match(['application/json', 'text/uri-list', 'text/html']) == 'application/json' \
                or request.values.get('_mediatype') == 'application/json':
            return Response(json.dumps(profiles), headers=headers)
        else:
            return render_template('profile_list.html', profiles=profiles, headers=headers)
    elif request.values.get('_profile') == 'tokens':
        # this request can only adhere to which profile
        headers = {'Content-Profile': '{}'.format('http://www.w3.org/ns/prof/')}  # TODO: address this meta profile

        mapping = metadata.list_profiles_tokens_uris_mappings_for_resource(request.base_url)

        # either return application/json or text/html
        if request.accept_mimetypes.best_match(['application/json', 'text/html']) == 'application/json' \
                or request.values.get('_mediatype') == 'application/json':
            return Response(json.dumps(mapping), headers=headers)
        else:
            return render_template('profile_mapping_list.html', mapping=mapping, headers=headers)
    # if both _profile=list & _mediatype=list, the profile listing wins
    elif request.values.get('_mediatype') == 'list' \
            or request.values.get('_mediatype').startswith('list,')\
            or request.values.get('_mediatype') == 'tokens' \
            or request.values.get('_mediatype').startswith('tokens,'):
        mediatype_metadata = metadata.get_mediatype_for_profile(
            request.base_url,
            profile_id=request.values.get('_profile'),
            mediatype_id=request.values.get('_mediatype')
        )

        # preserve the profile_id
        if mediatype_metadata[0] is not None:
            headers = {'Content-Profile': '{}'.format(mediatype_metadata[0])}
        else:
            headers = None

        if request.values.get('_mediatype') == 'list' or request.values.get('_mediatype').startswith('list,'):
            mediatypes_uris = metadata.list_mediatypes_for_resource_profile(
                request.base_url,
                profile_id=request.values.get('_profile'),
                return_only_uris=True,
            )

            # either return text/uri-list, application/json or text/html
            if request.accept_mimetypes.best_match(
                    ['application/json', 'text/uri-list', 'text/html']) == 'text/uri-list' \
                    or 'text/uri-list' in request.values.get('_mediatype'):
                return Response('\n'.join(mediatypes_uris), mimetype='text/uri-list', headers=headers)
            elif request.accept_mimetypes.best_match(
                    ['application/json', 'text/uri-list', 'text/html']) == 'application/json' \
                    or 'application/json' in request.values.get('_mediatype'):
                return Response(json.dumps(mediatypes_uris), headers=headers)
            else:
                return render_template('mediatype_list.html', profile=mediatype_metadata[0], mediatypes=mediatypes_uris)
        elif request.values.get('_mediatype') == 'tokens' or request.values.get('_mediatype').startswith('tokens,'):
            mapping = metadata.list_mediatypes_tokens_uris_mappings_for_resource(request.base_url, profile_id=mediatype_metadata[0])

            # either return application/json or text/html
            if request.accept_mimetypes.best_match(
                    ['application/json', 'text/uri-list', 'text/html']) == 'application/json' \
                    or 'application/json' in request.values.get('_mediatype'):
                return Response(json.dumps(mapping), headers=headers)
            else:
                return render_template('mediatype_mapping_list.html', profile=mediatype_metadata[0], mapping=mapping)
    else:
        # get the metadata for this resource/profile/mediatype
        mediatype_metadata = metadata.get_mediatype_for_profile(
            request.base_url,
            profile_id=request.values.get('_profile'),
            mediatype_id=request.values.get('_mediatype')
        )

        # preserve the profile_id
        if mediatype_metadata[0] is not None:
            headers['Content-Profile'] = '{}'.format(mediatype_metadata[0])

        # get the content for this resource/profile/mediatype from the relevant file
        with open(os.path.join(APP_DIR, 'data', mediatype_metadata[1].get('file')), 'r', encoding="utf-8") as f:
            response_content = f.read().replace('{{ BASE_URI }}', metadata.BASE_URI)

        return Response(
            response_content,
            mimetype=mediatype_metadata[1].get('token'),
            headers=headers
        )


if __name__ == '__main__':
   app.run(debug=True)
