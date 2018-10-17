import pytest
import pprint


BASE_URI = 'http://localhost:5000'
METADATA = {
    'research_papers': [
        {
            'description': 'No profiles, three Media Type',
            'uri': '/paper/1',
            'profiles': [
                {
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'text/html',
                            'file': 'paper-1.html',
                            'default': True
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'text/turtle',
                            'file': 'paper-1.ttl'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'application/ld+json',
                            'file': 'paper-1.json'
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
                            'token': 'text/html',
                            'file': 'paper-2-dct.html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'text/turtle',
                            'file': 'paper-2-dct.ttl',
                            'default': True
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'application/ld+json',
                            'file': 'paper-2-dct.json'
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
                    'token': 'epub',
                    'default': True,
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'text/html',
                            'file': 'paper-3-dct.html',
                            'default': True
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'text/turtle',
                            'file': 'paper-3-dct.ttl'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'application/ld+json',
                            'file': 'paper-3-dct.json'
                        },
                    ]
                },
                {
                    'uri': 'http://purl.org/dc/terms/',
                    'token': 'dct',
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'text/html',
                            'file': 'paper-3-dct.html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'text/turtle',
                            'file': 'paper-3-dct.ttl'
                        }
                    ]
                }
            ]
        }
    ],
    'licences': [
        {
            'uri': '/licence/1',
            'profiles': [
                {
                    'uri': 'https://creativecommons.org/ns#',
                    'token': 'cc',
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'text/html',
                            'default': True,
                            'file': 'licence-1-cc.html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/plain',
                            'token': 'text/plain',
                            'file': 'licence-1-cc.txt'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/xml',
                            'token': 'application/xml',
                            'file': 'licence-1-cc.xml'
                        },
                    ]

                },
                {
                    'uri': 'http://www.w3.org/ns/odrl',
                    'token': 'odrl',
                    'mediatypes': [
                        {
                            'uri': 'http://w3id.org/mediatype/text/html',
                            'token': 'text/html',
                            'default': True,
                            'file': 'licence-1-odrl.html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'text/turtle',
                            'file': 'licence-1-odrl.ttl'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'application/ld+json',
                            'file': 'licence-1-odrl.json'
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
                            'default': True,
                            'file': 'catalogue-reg.html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'text/turtle',
                            'file': 'catalogue-reg.ttl'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'application/ld+json',
                            'file': 'catalogue-reg.json'
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
                            'default': True,
                            'file': 'catalogue-aureg.html'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/text/turtle',
                            'token': 'text/turtle',
                            'file': 'catalogue-aureg.ttl'
                        },
                        {
                            'uri': 'http://w3id.org/mediatype/application/ld+json',
                            'token': 'application/ld+json',
                            'file': 'catalogue-auorg.json'
                        },
                    ]
                }
            ]
        }
    ]
}

'''
list resources
get resource - conneg options
list profiles
get profile
list media types for resource
get media type for resource
list media type for resource and profile
get media type for resource and profile
get resource
'''


class ResourceNotFoundException(Exception):
    def __init__(self):
        super().__init__('A Resource with that URI was not found.')


class ProfileNotFoundException(Exception):
    def __init__(self):
        super().__init__('A Profile with that ID was not found.')


class MediaTypeNotFoundException(Exception):
    def __init__(self):
        super().__init__('A Media Type with that ID was not found.')


def list_resources(return_only_uris=False):
    r = [x for x in METADATA['research_papers']]
    l = [x for x in METADATA['licences']]
    c = [x for x in METADATA['catalogues']]

    all = r + l + c

    if return_only_uris:
        return [BASE_URI + u.get('uri') for u in all]
    else:
        return all


def test_list_resource():
    expected = {
        'http://localhost:5000/paper/1',
        'http://localhost:5000/paper/2',
        'http://localhost:5000/paper/3',
        'http://localhost:5000/licence/1',
        'http://localhost:5000/catalogue'
    }
    assert set(list_resources(return_only_uris=True)) == expected


def get_resource_profconneg_options(resource_uri):
    resources = list_resources()
    y = [x for x in resources if BASE_URI + x.get('uri') == resource_uri]
    if y == []:
        raise ResourceNotFoundException()
    else:
        return y[0]


def test_get_resource_profconneg_options():
    expected = {
        'description': 'One profiles, three Media Type',
        'uri': '/paper/2',
        'profiles': [
            {
                'uri': 'http://purl.org/dc/terms/',
                'token': 'dct',
                'mediatypes': [
                    {
                        'uri': 'http://w3id.org/mediatype/text/html',
                        'token': 'text/html',
                        'file': 'paper-2-dct.html'
                    },
                    {
                        'uri': 'http://w3id.org/mediatype/text/turtle',
                        'token': 'text/turtle',
                        'file': 'paper-2-dct.ttl',
                        'default': True
                    },
                    {
                        'uri': 'http://w3id.org/mediatype/application/ld+json',
                        'token': 'application/ld+json',
                        'file': 'paper-2-dct.json'
                    },
                ]
            },
        ],
    }
    got = get_resource_profconneg_options(BASE_URI + '/paper/2')

    assert expected == got


def list_profiles_for_resource(resource_uri, return_only_uris=False):
    """
    resource with no profiles: /paper/1
    -> ([])

    resource with 1 profile: /paper/2
    -> (dct, http://purl.org/dc/terms/)

    resource with multiple profiles: /paper/3
    -> (epub, http://test.linked.data.gov.au/def/CSIRO-ePub-DCAP; dct, http://purl.org/dc/terms/)

    resource with multiple profiles, no default: /licence/1
    -> (cc, https://creativecommons.org/ns#; odrl, http://www.w3.org/ns/odrl)
    """
    # get the resource
    resource = get_resource_profconneg_options(resource_uri)

    # no profiles listed


    if return_only_uris:
        return [x.get('uri') for x in resource['profiles']]
    else:
        return resource['profiles']


def test_list_profiles_for_resource():
    assert list_profiles_for_resource(BASE_URI + '/paper/1', return_only_uris=True) == [None]

    assert list_profiles_for_resource(BASE_URI + '/paper/2', return_only_uris=True) == ['http://purl.org/dc/terms/']

    expected = {
        'http://test.linked.data.gov.au/def/CSIRO-ePub-DCAP',
        'http://purl.org/dc/terms/'
    }
    assert set(list_profiles_for_resource(BASE_URI + '/paper/3', return_only_uris=True)) == expected

    expected = {'https://creativecommons.org/ns#', 'http://www.w3.org/ns/odrl'}
    assert set(list_profiles_for_resource(BASE_URI + '/licence/1', return_only_uris=True)) == expected


def get_profile_for_resource(resource_uri, profile_id=None):
    """
    resource with no profiles: /paper/1
    -> {...}

    resource with 1 profile: /paper/2
    -> (dct, http://purl.org/dc/terms/)

    resource with multiple profiles: /paper/3
    -> (epub, http://test.linked.data.gov.au/def/CSIRO-ePub-DCAP; dct, http://purl.org/dc/terms/)

    resource with multiple profiles, no default: /licence/1
    -> (cc, https://creativecommons.org/ns#; odrl, http://www.w3.org/ns/odrl)
    """
    profiles = list_profiles_for_resource(resource_uri)

    # if no profile is declared, return the resource info directly
    if profile_id is not None:
        if profiles is None:
            return get_resource_profconneg_options(resource_uri)['profiles'][0]
        else:
            # if there is only one profile, return that
            if len(profiles) == 1:
                return profiles[0]
            else:
                # TODO: find profile by CURIE
                if profile_id.startswith('http'):
                    # Profile indicated by URI
                    profile = [x for x in profiles if x.get('uri') == profile_id][0]
                else:
                    # Profile indicated by token
                    profile = [x for x in profiles if x.get('token') == profile_id][0]

                return profile
    else:
        # no profile_id is set so just return any one
        return list_profiles_for_resource(resource_uri)[0]


def test_get_profile_for_resource():
    # no profiles listed so get default
    expected = {
        'mediatypes': [
            {
                'uri': 'http://w3id.org/mediatype/text/html',
                'token': 'text/html',
                'file': 'paper-1.html',
                'default': True
            },
            {
                'uri': 'http://w3id.org/mediatype/text/turtle',
                'token': 'text/turtle',
                'file': 'paper-1.ttl'
            },
            {
                'uri': 'http://w3id.org/mediatype/application/ld+json',
                'token': 'application/ld+json',
                'file': 'paper-1.json'
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
                'token': 'text/html',
                'file': 'paper-2-dct.html'
            },
            {
                'uri': 'http://w3id.org/mediatype/text/turtle',
                'token': 'text/turtle',
                'file': 'paper-2-dct.ttl',
                'default': True
            },
            {
                'uri': 'http://w3id.org/mediatype/application/ld+json',
                'token': 'application/ld+json',
                'file': 'paper-2-dct.json'
            }
        ]
    }
    got = get_profile_for_resource(BASE_URI + '/paper/2', 'http://purl.org/dc/terms/')
    assert expected == got

    # one profile only, select it by incorrect URI
    got = get_profile_for_resource(BASE_URI + '/paper/2', 'http://purl.org/dc/terms/x')
    assert expected == got

    # multiple profiles, select on by URI
    expected = {
        'uri': 'http://purl.org/dc/terms/',
        'token': 'dct',
        'mediatypes': [
            {
                'uri': 'http://w3id.org/mediatype/text/html',
                'token': 'text/html',
                'file': 'paper-3-dct.html'
            },
            {
                'uri': 'http://w3id.org/mediatype/text/turtle',
                'token': 'text/turtle',
                'file': 'paper-3-dct.ttl'
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
                'token': 'text/html',
                'default': True,
                'file': 'licence-1-odrl.html'
            },
            {
                'uri': 'http://w3id.org/mediatype/text/turtle',
                'token': 'text/turtle',
                'file': 'licence-1-odrl.ttl'
            },
            {
                'uri': 'http://w3id.org/mediatype/application/ld+json',
                'token': 'application/ld+json',
                'file': 'licence-1-odrl.json'
            },
        ]
    }
    got = get_profile_for_resource(BASE_URI + '/licence/1', 'odrl')
    assert expected == got


def list_mediatypes_for_resource_profile(resource_uri, profile_id=None, return_only_uris=False):
    mediatypes = get_profile_for_resource(resource_uri, profile_id).get('mediatypes')

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
    assert set(list_mediatypes_for_resource_profile(
        BASE_URI + '/paper/1',
        return_only_uris=True)) == expected

    assert set(list_mediatypes_for_resource_profile(
        BASE_URI + '/paper/1',
        profile_id='http://purl.org/dc/terms/',
        return_only_uris=True)) == expected

    assert set(list_mediatypes_for_resource_profile(
        BASE_URI + '/paper/1',
        profile_id='dct',
        return_only_uris=True)) == expected

    assert set(list_mediatypes_for_resource_profile(
        BASE_URI + '/paper/2',
        # no profile_id set
        return_only_uris=True)) == expected

    assert set(list_mediatypes_for_resource_profile(
        BASE_URI + '/paper/2',
        profile_id='http://purl.org/dc/terms/',
        return_only_uris=True)) == expected

    assert set(list_mediatypes_for_resource_profile(
        BASE_URI + '/paper/2',
        profile_id='dct',
        return_only_uris=True))

    expected = {
        'http://w3id.org/mediatype/text/html',
        'http://w3id.org/mediatype/text/turtle',
        'http://w3id.org/mediatype/application/ld+json'
    }
    assert expected == set(list_mediatypes_for_resource_profile(
        BASE_URI + '/licence/1',
        profile_id='odrl',
        return_only_uris=True))

    # incorrect URI
    with pytest.raises(ResourceNotFoundException):
        set(list_mediatypes_for_resource_profile(
            BASE_URI + '/paper/23',
            profile_id='dct',
            return_only_uris=True))

    # incorrect profile_id
    expected = {
        'http://w3id.org/mediatype/text/html',
        'http://w3id.org/mediatype/application/ld+json',
        'http://w3id.org/mediatype/text/turtle'
    }
    assert set(list_mediatypes_for_resource_profile(
        BASE_URI + '/paper/2',
        profile_id='xxx',
        return_only_uris=True)) == expected


def get_mediatype_for_response_profile(resource_uri, profile_id=None, mediatype_id=None):
    profile = get_profile_for_resource(resource_uri, profile_id)
    if mediatype_id.startswith('http'):
        mediatype = [x for x in profile['mediatypes'] if x.get('uri') == mediatype_id][0]
    else:
        mediatype = [x for x in profile['mediatypes'] if x.get('token') == mediatype_id][0]

    if mediatype is None:
        return profile[0]  # TODO: replace first with default
    else:
        return mediatype


def test_get_mediatype_for_response_profile():
    expected = {
        'uri': 'http://w3id.org/mediatype/text/turtle',
        'token': 'text/turtle',
        'file': 'paper-3-dct.ttl'
    }
    assert expected == get_mediatype_for_response_profile(BASE_URI + '/paper/3', profile_id='epub', mediatype_id='text/turtle')

    got = get_mediatype_for_response_profile(BASE_URI + '/catalogue', mediatype_id='application/ld+json').get('file')
    assert 'catalogue-reg.json' == got


def test_all():
    # test_list_resource()
    # print('completed test_list_resource()')
    # test_get_resource_profconneg_options()
    # print('completed test_get_resource_profconneg_options()')
    # test_list_profiles_for_resource()
    # print('completed test_list_profiles_for_resource()')
    # test_get_profile_for_resource()
    # print('completed test_get_profile_for_resource()')
    # test_list_mediatypes_for_resource_profile()
    # print('completed test_list_mediatypes_for_resource_profile()')
    test_get_mediatype_for_response_profile()
    print('completed test_get_mediatype_for_responce_profile()')


if __name__ == '__main__':
    print('Testing data.pay...')
    test_all()
