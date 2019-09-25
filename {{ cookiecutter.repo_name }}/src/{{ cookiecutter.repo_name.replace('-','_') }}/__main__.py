import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)


from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }} import {{ cookiecutter.project_name.replace('-', '').replace('_', '').title().replace(' ', '') }}

