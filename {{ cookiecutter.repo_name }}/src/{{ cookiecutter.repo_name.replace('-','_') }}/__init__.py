import os
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIG_INI = os.path.join(BASE_DIR, 'config.ini')
LOGGER_CONFIG = os.path.join(BASE_DIR, 'logger.conf')
STATIC_DIR = os.path.join(os.path.dirname(BASE_DIR), 'docs')
SETTINGS_FILE = os.path.join(BASE_DIR, 'settings.py')


import logging
import logging.config
print "Logger config location", LOGGER_CONFIG
logging.config.fileConfig(LOGGER_CONFIG)
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

from eazyserver import Eazy
app = Eazy(__name__, settings=SETTINGS_FILE, configs=[DEFAULT_CONFIG_INI], env_prefix='APP_')
app.config['SWAGGER_HOST'] = app.config['HOST_NAME']

from eazyserver.rpc.exceptions import *

import core
