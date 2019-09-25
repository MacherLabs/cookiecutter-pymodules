"""
    SETTINGS
    ~~~~~~~~~~~~~~~~~

    Settings file for {{ cookiecutter.repo_name.replace('-','_') }}.

    :license: Proprietary, see LICENSE for more details.
"""
import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

import os

SWAGGER_INFO = {
    'title': '{{ cookiecutter.project_name }}',
    'version': '{{ cookiecutter.version }}',
    'description': '{{ cookiecutter.project_short_description }}',
    'termsOfService': 'terms of service',
    'contact': {
        'name': '{{ cookiecutter.organization_name }}',
        'url': '{{ cookiecutter.organization_website }}'
    },
    'license': {
        'name': 'BSD',
        'url': 'https://github.com/pyeve/eve-swagger/blob/master/LICENSE',
    },
    'schemes': ['https','http'],
}

DOMAIN = {}
