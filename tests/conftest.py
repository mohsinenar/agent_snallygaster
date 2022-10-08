"""conftest.py for agent Fingerprint Generator. """
import pathlib

import pytest
from ostorlab.agent import definitions as agent_definitions
from ostorlab.agent.message import message as msg
from ostorlab.runtimes import definitions as runtime_definitions

from agent import snallygaster_agent

OSTORLAB_YAML_PATH = (pathlib.Path(__file__).parent.parent / 'ostorlab.yaml').absolute()


@pytest.fixture
def scan_message_domain_name() -> msg.Message:
    """Creates a dummy message of type v3.asset.ip.v4.port.service to be used by the agent for testing purposes.
    """
    selector = 'v3.asset.domain_name'
    msg_data = {'name': ' zero.webappsecurity.com'}
    return msg.Message.from_data(selector, data=msg_data)


@pytest.fixture
def test_agent() -> snallygaster_agent.SnallyGasterAgent:
    with open(OSTORLAB_YAML_PATH, 'r', encoding='utf-8') as yaml_o:
        definition = agent_definitions.AgentDefinition.from_yaml(yaml_o)
        settings = runtime_definitions.AgentSettings(
            key='agent/ostorlab/agent_snallygaster_generator',
            redis_url='redis://redis')
        return snallygaster_agent.SnallyGasterAgent(definition, settings)
