BASE_URI = 'http://localhost'
DATA = {
    'research_papers': [
        {
            'uri': '/paper/1',
            'profiles': [
                {
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'turtle'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'json-ld'
                        },
                    ]
                }
            ]
        },
        {
            'uri': '/paper/2',
            'profiles': [
                {
                    'uri': 'http://purl.org/dc/terms/',
                    'token': 'dct',
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'turtle'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'json-ld'
                        },
                    ]
                },
            ],
        },
        {
            'uri': '/paper/3',
            'profiles': [
                {
                    'uri': 'http://linked.data.gov.au/dataset/CSIRO-ePub-DCAP',
                    'token': 'epub-dcap',
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'turtle'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'json-ld'
                        },
                    ]
                },
                {
                    'uri': 'http://purl.org/dc/terms/',
                    'token': 'dct',
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'turtle'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'json-ld'
                        },
                    ]
                }
            ]
        }
    ],
    'licences': [
        {
            'uri': '/license/1',
            'profiles': [
                {
                    'uri': 'https://creativecommons.org/ns#',
                    'token': 'cc',
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/plain',
                            'token': 'text'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/xml',
                            'token': 'xml'
                        },
                    ]

                },
                {
                    'uri': 'http://www.w3.org/ns/odrl',
                    'token': 'odrl2',
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'turtle'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'json-ld'
                        },
                    ]
                }
            ]
        }
    ],
    'catalogues': [
        {
            'uri': '/catalogue',
            'profiles': [
                {
                    'uri': 'http://purl.org/linked-data/registry#',
                    'token': 'reg',
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'turtle'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'json-ld'
                        },
                    ]
                },
                {
                    'uri': 'http://example.org/ns/ausreg',
                    'token': 'ausreg',
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'turtle'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'json-ld'
                        },
                    ]
                }
            ]
        }
    ]
}
