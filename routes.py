from flask import Flask, Blueprint, render_template, request, redirect, url_for, abort, jsonify, Response
from rdflib import Graph, RDF, RDFS, Literal, URIRef, XSD, OWL, BNode

app = Flask(__name__)


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

    return Response(html)


if __name__ == '__main__':
   app.run()
