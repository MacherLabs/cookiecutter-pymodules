import logging
logger = logging.getLogger(__name__)
logger.info("Loaded " + __name__)


from {{ cookiecutter.repo_name.replace('-','_') }} import app

from eazyserver.core.kafka_connector import KafkaConnector
from .core.{{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }} import {{ cookiecutter.project_name.replace('-', '').replace('_', '').title().replace(' ', '') }}
from eazyserver.core.manager import Manager

config = dict(app.config)
#TODO: Get Config from cloud 

kafka_client_type = config["KAFKA_CLIENT_TYPE"] 

kafka_client_config = {}
kafka_client_config["broker"] = config["KAFKA_BROKER"]
kafka_client_config["sync_consumers"] = config["KAFKA_SYNC_CONSUMER"]

kafka_client_config["producer_topic"] = config["KAFKA_PRODUCER_TOPIC"]
kafka_client_config["producer_params"] = config["KAFKA_PRODUCER_PARAMS"]

kafka_client_config["consumer_1_topic"] = config["KAFKA_CONSUMER_1_TOPIC"]
kafka_client_config["consumer_1_params"] = config["KAFKA_CONSUMER_1_PARAMS"]

kafka_client_config["consumer_2_topic"] = config["KAFKA_CONSUMER_2_TOPIC"]
kafka_client_config["consumer_2_params"] = config["KAFKA_CONSUMER_2_PARAMS"]

signal_map = {}


manager = Manager(
                    behaviour={{ cookiecutter.project_name.replace('-', '').replace('_', '').title().replace(' ', '') }}(config['BEHAVIOUR_CONFIG']), 
                    connector_type="kafka",
                    kafka_client_type=kafka_client_type,
                    kafka_client_config=kafka_client_config,
                    signal_map=signal_map)

manager.onStart()
manager.onSignal()
manager.run()
manager.onExit()


