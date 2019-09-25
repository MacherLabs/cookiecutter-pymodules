import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)


class {{ cookiecutter.project_name.replace('-', '').replace('_', '').title().replace(' ', '') }}(Behaviour):
    def __init__(self, Config):
        super({{ cookiecutter.project_name.replace('-', '').replace('_', '').title().replace(' ', '') }},  self).__init__(Config)
        self.config = Config
        
    def run(self, data=None):
        res = {}

        return res
