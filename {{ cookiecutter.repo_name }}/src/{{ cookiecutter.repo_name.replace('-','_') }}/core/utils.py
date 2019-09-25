import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)

import json
from eve.utils import str_to_date, date_to_rfc1123
from {{ cookiecutter.repo_name.replace('-','_') }} import app

