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
                            'token': 'text/html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'text/turtle'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'application/ld+json'
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
                            'token': 'text/html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'text/turtle'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'application/ld+json'
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
                    'uri': 'http://test.linked.data.gov.au/def/CSIRO-ePub-DCAP',
                    'token': 'epub-dcap',
                    'default': True,
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'text/html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'text/turtle'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'application/ld+json'
                        },
                    ]
                },
                {
                    'uri': 'http://purl.org/dc/terms/',
                    'token': 'dct',
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'text/html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/xml',
                            'token': 'text/turtle'
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
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'text/html',
                            'default': True
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/plain',
                            'token': 'text/plain'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/xml',
                            'token': 'application/xml'
                        },
                    ]

                },
                {
                    'uri': 'http://www.w3.org/ns/odrl',
                    'token': 'odrl',
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'text/html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'text/turtle'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'application/ld+json'
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
                            'token': 'text/html',
                            'default': True
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'text/turtle'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'application/ld+json'
                        },
                    ]
                },
                {
                    'uri': 'http://example.org/ns/ausreg',
                    'token': 'ausreg',
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'text/html',
                            'default': True
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'text/turtle'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'application/ld+json'
                        },
                    ]
                }
            ]
        }
    ]
}

'''
list resources
get resource
list profiles
get profile
list media types for resource
get media type for resource
list media type for resource and profile
get media type for resource and profile
'''


def list_resources(return_only_uris=False):
    r = [x for x in DATA['research_papers']]
    l = [x for x in DATA['licences']]
    c = [x for x in DATA['catalogues']]

    all = r + l + c

    if return_only_uris:
        return [BASE_URI + u.get('uri') for u in all]
    else:
        return all


def get_resource_profconneg_options(resource_uri):
    resources = list_resources()
    return [x for x in resources if BASE_URI + x.get('uri') == resource_uri][0]


def list_profiles_for_resource(resource_uri, return_only_uris=False):
    """
    resource with no profiles: /paper/1
    -> ([])

    resource with 1 profile: /paper/2
    -> (dct, http://purl.org/dc/terms/)

    resource with multiple profiles: /paper/3
    -> (epub-dcap, http://test.linked.data.gov.au/def/CSIRO-ePub-DCAP; dct, http://purl.org/dc/terms/)

    resource with multiple profiles, no default: /license/1
    -> (cc, https://creativecommons.org/ns#; odrl, http://www.w3.org/ns/odrl)
    """
    # get the resource
    resource = get_resource_profconneg_options(resource_uri)

    # no profiles listed
    if len(resource['profiles']) == 1:
        if resource['profiles'][0].get('token') is None:
            return None

    if return_only_uris:
        return [x.get('uri') for x in resource['profiles']]
    else:
        return resource['profiles']


def test_list_profiles_for_resource():
    assert list_profiles_for_resource(BASE_URI + '/paper/1', return_only_uris=True) is None

    assert list_profiles_for_resource(BASE_URI + '/paper/2', return_only_uris=True) == ['http://purl.org/dc/terms/']

    expected = {
        'http://test.linked.data.gov.au/def/CSIRO-ePub-DCAP',
        'http://purl.org/dc/terms/'
    }
    assert set(list_profiles_for_resource(BASE_URI + '/paper/3', return_only_uris=True)) == expected

    expected = {'https://creativecommons.org/ns#', 'http://www.w3.org/ns/odrl'}
    assert set(list_profiles_for_resource(BASE_URI + '/license/1', return_only_uris=True)) == expected


def get_profile_for_resource(resource_uri, profile_id):
    """
    resource with no profiles: /paper/1
    -> {...}

    resource with 1 profile: /paper/2
    -> (dct, http://purl.org/dc/terms/)

    resource with multiple profiles: /paper/3
    -> (epub-dcap, http://test.linked.data.gov.au/def/CSIRO-ePub-DCAP; dct, http://purl.org/dc/terms/)

    resource with multiple profiles, no default: /license/1
    -> (cc, https://creativecommons.org/ns#; odrl, http://www.w3.org/ns/odrl)
    """
    profiles = list_profiles_for_resource(resource_uri)

    # if no profile is declared, return the resource info directly
    if profiles is None:
        return get_resource_profconneg_options(resource_uri)['profiles'][0]
    else:
        # if there is only one profile, return that
        if len(profiles) == 1:
            return profiles[0]
        else:
            # TODO: find profile by qname
            if profile_id.startswith('http'):
                # Profile indicated by URI
                return [x for x in profiles if x.get('uri') == profile_id][0]
            else:
                # Profile indicated by token
                return [x for x in profiles if x.get('token') == profile_id][0]


def test_get_profile_for_resource():
    # no profiles listed so get default
    expected = {
        'mediatypes': [
            {
                'uri': 'http://w3id.org/mediatype/text/html',
                'token': 'text/html'
            },
            {
                'uri': 'http://w3id.org/mediatype/text/turtle',
                'token': 'text/turtle'
            },
            {
                'uri': 'http://w3id.org/mediatype/application/ld+json',
                'token': 'application/ld+json'
            },
        ]
    }
    got = get_profile_for_resource(BASE_URI + '/paper/1', 'http://purl.org/dc/terms/')
    assert expected == got

    # one profile only, select it by URI
    expected = {
        'uri': 'http://purl.org/dc/terms/',
        'token': 'dct',
        'mediatypes': [
            {
                'uri': 'http://w3id.org/mediatype/text/html',
                'token': 'text/html'
            },
            {
                'uri': 'http://w3id.org/mediatype/text/turtle',
                'token': 'text/turtle'
            },
            {
                'uri': 'http://w3id.org/mediatype/application/ld+json',
                'token': 'application/ld+json'
            },
        ]
    }
    got = get_profile_for_resource(BASE_URI + '/paper/2', 'http://purl.org/dc/terms/')
    assert expected == got

    # one profile only, select it by incorrect URI
    expected = {
        'uri': 'http://purl.org/dc/terms/',
        'token': 'dct',
        'mediatypes': [
            {
                'uri': 'http://w3id.org/mediatype/text/html',
                'token': 'text/html'
            },
            {
                'uri': 'http://w3id.org/mediatype/text/turtle',
                'token': 'text/turtle'
            },
            {
                'uri': 'http://w3id.org/mediatype/application/ld+json',
                'token': 'application/ld+json'
            },
        ]
    }
    got = get_profile_for_resource(BASE_URI + '/paper/2', 'http://purl.org/dc/terms/x')
    assert expected == got

    # multiple profiles, select on by URI
    expected = {
        'uri': 'http://purl.org/dc/terms/',
        'token': 'dct',
        'mediatypes': [
            {
                'uri': 'http://w3id.org/mediatype/text/html',
                'token': 'text/html'
            },
            {
                'uri': 'http://w3id.org/mediatype/application/xml',
                'token': 'text/turtle'
            }
        ]
    }
    got = get_profile_for_resource(BASE_URI + '/paper/3', 'http://purl.org/dc/terms/')
    assert expected == got

    # multi profiles, select one by token
    expected = {
        'uri': 'http://www.w3.org/ns/odrl',
        'token': 'odrl',
        'mediatypes': [
            {
                'uri': 'http://w3id.org/mediatype/text/html',
                'token': 'text/html'
            },
            {
                'uri': 'http://w3id.org/mediatype/text/turtle',
                'token': 'text/turtle'
            },
            {
                'uri': 'http://w3id.org/mediatype/application/ld+json',
                'token': 'application/ld+json'
            },
        ]
    }
    got = get_profile_for_resource(BASE_URI + '/license/1', 'odrl')
    assert expected == got


def list_mediatypes_for_resource_profile(resource_uri, profile_id=None, return_only_uris=False):
    # get profiles for the resource, even if None
    profiles = list_profiles_for_resource(resource_uri)

    if profiles is None:
        mediatypes = get_resource_profconneg_options(resource_uri)['profiles']
    else:
        mediatypes = [x.get('mediatypes') for x in profiles if x.get('token') == profile_id]

    if return_only_uris:
        return [x.get('uri') for x in mediatypes]
    else:
        return mediatypes


def test_list_mediatypes_for_resource_profile():
    expected = {
        'http://w3id.org/mediatype/text/html',
        'http://w3id.org/mediatype/text/turtle',
        'http://w3id.org/mediatype/application/ld+json'
    }
    assert set(list_mediatypes_for_resource_profile(BASE_URI + '/paper/1', return_only_uris=True)) == expected

    assert set(list_mediatypes_for_resource_profile(
        BASE_URI + '/paper/1',
        profile_id='http://purl.org/dc/terms/',
        return_only_uris=True)) == expected

    assert set(list_mediatypes_for_resource_profile(
        BASE_URI + '/paper/1',
        profile_id='dct',
        return_only_uris=True)) == expected

    assert set(list_mediatypes_for_resource_profile(BASE_URI + '/paper/2', return_only_uris=True)) == expected

    assert set(list_mediatypes_for_resource_profile(
        BASE_URI + '/paper/2',
        profile_id='http://purl.org/dc/terms/',
        return_only_uris=True)) == expected

    got = set(list_mediatypes_for_resource_profile(
        BASE_URI + '/paper/2',
        profile_id='dct',
        return_only_uris=True))
    print(got)
    assert got == expected


def get_resource(resource_uri, profile_id=None, mediatype_id=None):
    pass


if __name__ == '__main__':
    print('Testing data.pay...')

    test_list_mediatypes_for_resource_profile()
