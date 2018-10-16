from flask import Flask, Blueprint, render_template, request, redirect, url_for, abort, jsonify, Response
from rdflib import Graph, RDF, RDFS, Literal, URIRef, XSD, OWL, BNode

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
# TODO: 3x register
# TODO: 3x instance accessors


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
  </body>
</html>'''.format(
        title='Profile Conneg QSA Demonstrator'
    )
    # TODO: add about info here
    # TODO: add implemented instance info here

    return Response(html)


if __name__ == '__main__':
   app.run()
