"""Unittests for agent."""
import json
from typing import List, Union, Dict

from ostorlab.agent.message import message as msg
from pytest_mock import plugin

from agent import snallygaster_agent


def testSnallyGasterAgent_whenSubDomainVulnerabilityIsFound_thenVulnerabilityIsReported(
        test_agent: snallygaster_agent.SnallyGasterAgent,
        agent_mock: List[msg.Message],
        mocker: plugin.MockerFixture,
        scan_message_domain_name: msg.Message,
        agent_persist_mock: Dict[Union[str, bytes], Union[str, bytes]]) -> None:
    """Test that a vulnerability is reported when a subdomain is found."""
    mocker.patch('agent.snallygaster_agent._run_snallygaster_command', return_value=json.loads(
        '[{"cause": "apache_server_status", "url": "http://zero.webappsecurity.com/server-status", "misc": ""}]'))
    test_agent.process(scan_message_domain_name)
    test_agent.process(scan_message_domain_name)

    assert len(agent_mock) == 1
    assert agent_mock[0].data.get('title') == 'Generic Web Entry'
    assert 'http://zero.webappsecurity.com/server-status' in agent_mock[0].data.get('technical_detail', '')
