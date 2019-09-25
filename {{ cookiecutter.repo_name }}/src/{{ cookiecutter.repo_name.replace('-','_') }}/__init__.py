import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
LOGGER_CONFIG = os.path.join(os.path.dirname(BASE_DIR), 'logger.conf')
STATIC_DIR = os.path.join(os.path.dirname(BASE_DIR), 'docs')
SETTINGS_FILE = os.path.join(BASE_DIR, 'settings.py')


import logging
import logging.config
print("Logger config location:{}".format(LOGGER_CONFIG))
logging.config.fileConfig(LOGGER_CONFIG)
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

from {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }} import {{ cookiecutter.project_name.replace('-', '').replace('_', '').title().replace(' ', '') }}
