import os
from flask import Flask, Blueprint, render_template, request, redirect, url_for, abort, jsonify, Response
from rdflib import Graph, RDF, RDFS, Literal, URIRef, XSD, OWL, BNode
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
    html = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body>
    <h1>{title}</h1>
    <p>
      This small <a href="https://www.python.org/">Python</a> <a href="http://flask.pocoo.org/">Flask</a> web 
      application that demonstrates profile-based content negotiation, as per the developing <em>profile</em> 
      specifications from the <a href="https://www.w3.org/2017/dxwg/">Dataset Exchange Working Group</a>.
    </p>
    <p>
      Specifically, this API is a realisation of the <a href="https://w3c.github.io/dxwg/conneg-by-ap/">Content 
      Negotiation by Profile</a>'s <a href="https://w3c.github.io/dxwg/conneg-by-ap/#abstractmodel">Abstract Model</a>.     
    </p>
    <h2>Resources</h2>
    <ul>
        <li><a href="/paper/1">{BASE_URI}/paper/1</a> - a scientific paper</li>
        <li><a href="/paper/2">{BASE_URI}/paper/2</a></li>
        <li><a href="/paper/3">{BASE_URI}/paper/3</a></li>
        <li><a href="/license/1">{BASE_URI}/license/1</a> - a license for an asset such as a dataset</li>
        <li><a href="/catalogue">{BASE_URI}/catalogue</a> - a <a href="https://www.w3.org/TR/vocab-dcat-2/">DCAT</a>-style catalogue</li>
    </ul>
  </body>
</html>'''.format(
        title='Profile Conneg QSA Demonstrator',
        BASE_URI=metadata.BASE_URI
    )
    # TODO: add about info here
    # TODO: add implemented instance info here

    return Response(html)


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
    uri = metadata.BASE_URI + request.path

    # validate input
    try:
        validate_qsas()
    except QueryStringArgumentError as e:
        return Response(str(e), status=404, mimetype='text/plain')

    # special cases - listing
    if request.values.get('_profile') == 'list':
        profiles_uris = metadata.list_profiles_for_resource(uri, return_only_uris=True)

        return Response('\n'.join(profiles_uris), mimetype='text/uri-list')
    elif request.values.get('_mediatype') == 'list':
        mediatype_metadata = metadata.get_mediatype_for_response_profile(
            uri,
            profile_id=request.values.get('_profile'),
            mediatype_id=request.values.get('_mediatype')
        )

        # preserve the profile_id
        if mediatype_metadata[0] is not None:
            headers = {'Content-Profile': '{}'.format(mediatype_metadata[0])}
        else:
            headers = None

        mediatypes_uris = metadata.list_mediatypes_for_resource_profile(
            uri,
            profile_id=request.values.get('_profile'),
            return_only_uris=True,
        )

        return Response('\n'.join(mediatypes_uris), mimetype='text/uri-list', headers=headers)
    else:
        # get the metadata for this resource/profile/mediatype
        mediatype_metadata = metadata.get_mediatype_for_response_profile(
            uri,
            profile_id=request.values.get('_profile'),
            mediatype_id=request.values.get('_mediatype')
        )

        # preserve the profile_id
        if mediatype_metadata[0] is not None:
            headers = {'Content-Profile': '{}'.format(mediatype_metadata[0])}
        else:
            headers = None

        # get the content for this resource/profile/mediatype from the relevant file
        response_content = open(
            os.path.join(APP_DIR, 'data', mediatype_metadata[1].get('file')), 'r'
        ).read().replace('{{ BASE_URI }}', metadata.BASE_URI)

        return Response(
            response_content,
            mimetype=mediatype_metadata[1].get('token'),
            headers=headers
        )


if __name__ == '__main__':
   app.run()
