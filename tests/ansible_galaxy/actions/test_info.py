
import logging
import mock

from ansible_galaxy.actions import info

log = logging.getLogger(__name__)


def display_callback(msg, **kwargs):
    log.debug(msg)


def test_info_empty(galaxy_context):
    ret = info.info_repository_specs(galaxy_context,
                                     # mock api
                                     mock.Mock(),
                                     [],
                                     display_callback=display_callback,
                                     offline=True)

    log.debug('ret: %s', ret)


def test_info(galaxy_context):
    ret = info.info_repository_specs(galaxy_context,
                                     # mock api
                                     mock.Mock(),
                                     ['namespace.repo.content'],
                                     display_callback=display_callback,
                                     offline=True)

    log.debug('ret: %s', ret)


def test_repr_remote_repo():
    data = {'summary_fields':
            {'namespace': {'name': 'some_namespace'},
             'content_objects': [{'name': 'some_content',
                                  'content_type': 'role',
                                  'description': 'Description of some content object'}],
             'versions': [],
             },
            'name': 'some_name',
            'description': 'Description of some remote repo',
            'clone_url': 'http://github.com/alikins/some_repo',
            'format': 'multi',
            }
    res = info._repr_remote_repo(data)
    log.debug('res: %s', res)

    assert 'Description of some remote repo'in res


def test_repr_role_info():
    data = {'name': 'some_role',
            'description': 'Description of some_role',
            'some_other_info': 'foo bar',
            'some_dict': {'polarity': 'negative',
                          'description': 'another description?',
                          'coolness': 'not at all'},
            }
    res = info._repr_role_info(data)

    log.debug('res: %s', res)

    assert 'some_role' in res
    assert 'Description of some_role' in res
