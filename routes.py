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


@app.route('/')
def home():
    return render_template('home.html', BASE_URI=metadata.BASE_URI)


class QueryStringArgumentError(Exception):
    def __init__(self):
        super().__init__('Query String Arguments must have the keys _profile or _mediatype.')


def validate_qsas():
    for key, value in request.values.items():
        if key not in ['_profile', '_mediatype']:
            raise QueryStringArgumentError()


def is_preferred_mediatype(request, mediatype_id):
    return request.accept_mimetypes.best_match(['application/json', 'text/uri-list', 'text/html']) == mediatype_id \
           or request.values.get('_mediatype') == mediatype_id


@app.route('/catalogue')
@app.route('/paper/<string:id>')
@app.route('/license/<string:id>')
def resource(id=None):
    '''
    1. Validate input
    2. Make Link headers
    3. Handle list requests
    4. Handle tokens requests
    5. Handle direct resource/profile/Media Type requests
    '''
    # 1. Validate input
    try:
        validate_qsas()
    except QueryStringArgumentError as e:
        return Response(str(e), status=400, mimetype='text/plain')

    if request.values.get('_profile') is not None:
        profile_ids = request.values.get('_profile').split(',')
    else:
        profile_ids = ['']

    if request.values.get('_mediatype') is not None:
        mediatype_ids = request.values.get('_mediatype').split(',')
    else:
        mediatype_ids = ['']

    # 3. Handle list requests
    if profile_ids[0] == 'list':
        profiles = metadata.list_profiles_for_resource(request.base_url, return_only_uris=True)

        # this request can only adhere to this profile
        headers = {'Content-Profile': '{}'.format('http://www.w3.org/ns/prof/')}  # TODO: address this meta profile
        # either return a text/uri-list, application/json or text/html
        if is_preferred_mediatype(request, 'text/uri-list') \
                or is_preferred_mediatype(request, 'https://w3id.org/mediatype/text/uri-list'):
            return Response('\n'.join(profiles), mimetype='text/uri-list', headers=headers)
        elif is_preferred_mediatype(request, 'application/json') \
                or is_preferred_mediatype(request, 'https://w3id.org/mediatype/application/json'):
            return Response(json.dumps(profiles), headers=headers)
        else:
            return render_template('profile_list.html', profiles=profiles, headers=headers)
    elif profile_ids[0] == 'tokens':
        # 4. Handle tokens requests
        headers = {'Content-Profile': '{}'.format('http://www.w3.org/ns/prof/')}  # TODO: address this meta profile

        mapping = metadata.list_profiles_tokens_uris_mappings_for_resource(request.base_url)

        # either return application/json or text/html
        if is_preferred_mediatype(request, 'application/json') \
                or is_preferred_mediatype(request, 'https://w3id.org/mediatype/application/json'):
            return Response(json.dumps(mapping), headers=headers)
        else:
            return render_template('profile_mapping_list.html', mapping=mapping, headers=headers)
    # if both _profile=list & _mediatype=list, the profile listing wins
    elif mediatype_ids[0] == 'list' or mediatype_ids[0] == 'tokens':
        mediatype_metadata = metadata.get_mediatype_for_profile(
            request.base_url,
            profile_ids=profile_ids,
            mediatype_ids=mediatype_ids
        )

        # preserve the profile_id
        if mediatype_metadata[0] is not None:
            headers = {'Content-Profile': '{}'.format(mediatype_metadata[0])}
        else:
            headers = None

        # 3. Handle list requests
        if mediatype_ids[0] == 'list':
            mediatypes_uris = metadata.list_mediatypes_for_resource_profile(
                request.base_url,
                profile_ids=profile_ids,
                return_only_uris=True,
            )

            # TODO: cater for conneg & QSA mediatype[1]
            # either return text/uri-list, application/json or text/html
            if request.accept_mimetypes.best_match(
                    ['application/json', 'text/uri-list', 'text/html']) == 'text/uri-list' \
                    or 'text/uri-list' in mediatype_ids:
                return Response('\n'.join(mediatypes_uris), mimetype='text/uri-list', headers=headers)
            elif request.accept_mimetypes.best_match(
                    ['application/json', 'text/uri-list', 'text/html']) == 'application/json' \
                    or 'application/json' in mediatype_ids:
                return Response(json.dumps(mediatypes_uris), headers=headers)
            else:
                return render_template('mediatype_list.html', profile=mediatype_metadata[0], mediatypes=mediatypes_uris)
        # 4. Handle tokens requests
        elif mediatype_ids[0] == 'tokens':
            mapping = metadata.list_mediatypes_tokens_uris_mappings_for_resource(
                request.base_url, profile_ids=mediatype_metadata[0]
            )

            # either return application/json or text/html
            if request.accept_mimetypes.best_match(
                    ['application/json', 'text/uri-list', 'text/html']) == 'application/json' \
                    or 'application/json' in mediatype_ids:
                return Response(json.dumps(mapping), headers=headers)
            else:
                return render_template('mediatype_mapping_list.html', profile=mediatype_metadata[0], mapping=mapping)
    # 5. Handle direct resource/profile/Media Type requests
    else:
        return metadata.get_response(request, profile_ids=profile_ids, mediatype_ids=mediatype_ids)


if __name__ == '__main__':
    from flaskext.markdown import Markdown

    Markdown(app)
    app.run(debug=True)
