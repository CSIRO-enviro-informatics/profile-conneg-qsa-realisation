BASE_URI = 'http://localhost:5000'
DATA = {
    'research_papers': [
        {
            'description': 'No profiles, three Media Type',
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
            'description': 'One profiles, three Media Type',
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
            'description': 'Two profiles, three Media Type for one, two for the other',
            'uri': '/paper/3',
            'profiles': [
                {
                    'uri': 'http://linked.data.gov.au/dataset/CSIRO-ePub-DCAP',
                    'token': 'epub-dcap',
                    'default': True,
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
                            'uri': 'http://w3id.org/mediatype/application/xml',
                            'token': 'turtle'
                        }
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
                    'default': True,
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'html',
                            'default': True
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
                    'default': True,
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'html',
                            'default': True
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
                            'token': 'html',
                            'default': True
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


def get_resources(return_only_uris=False):
    r = [x for x in DATA['research_papers']]
    l = [x for x in DATA['licences']]
    c = [x for x in DATA['catalogues']]

    all = r + l + c

    if return_only_uris:
        return [BASE_URI + u.get('uri') for u in all]
    else:
        return all


def get_resource(uri):
    resources = get_resources()
    return [x for x in resources if BASE_URI + x.get('uri') == uri][0]


def get_profiles_for_resource(uri, return_only_uris=False):
    # get the resource
    resource = get_resource(uri)

    # no profiles listed
    if len(resource['profiles']) == 1:
        if resource['profiles'][0].get('token') is None:
            return None

    if return_only_uris:
        return [x.get('uri') for x in resource['profiles']]
    else:
        return resource['profiles']


def get_mediatypes_for_resource_profile(resource_uri, profile_id=None, return_only_uris=False):
    # get profiles for the resource, even if None
    profiles = get_profiles_for_resource(resource_uri)

    # no profiles
    if profiles is None:
        # just get the Media Types for the Resource
        return get_resource(resource_uri).get('profiles')[0].get('mediatypes')

    # profiles
    if not profile_id:
        # no profile ID is set so return Media Types for default profile
        if len(profiles) == 1:  # when there's only one Profile
            return profiles[0].get('mediatypes')
        else:  # when there're multiple Profiles with a default listed
            return [x.get('mediatypes') for x in profiles if x.get('default') == True][0]

    else:  # a specific Profile is specified by either token or URI
        if profile_id.startswith('http'):
            # Profile indicated by URI
            return [x.get('mediatypes') for x in profiles if x.get('uri') == profile_id][0]
        else:
            # Profile indicated by token
            return [x.get('mediatypes') for x in profiles if x.get('token') == profile_id][0]


if __name__ == '__main__':
    print('Testing data.pay...')

    # print Media Types for Paper 1

    import pprint
    # pprint.pprint(get_mediatypes_for_resource('http://localhost:5000/paper/2'))
    # pprint.pprint(get_resources(return_only_uris=True))
    # pprint.pprint(get_profiles_for_resource('http://localhost:5000/paper/1', return_only_uris=True))
    # http://purl.org/dc/terms/
    pprint.pprint(get_mediatypes_for_resource_profile(BASE_URI + '/paper/3', 'http://purl.org/dc/terms/'))
