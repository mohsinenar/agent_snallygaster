"""dnsReaper [https://github.com/punk-security/dnsReaper](dnsReaper) tool implementation as ostorlab agent"""
import json
import logging
import subprocess
from typing import List, Dict, Any

from ostorlab.agent import agent, definitions as agent_definitions
from ostorlab.agent.kb import kb
from ostorlab.agent.message import message as msg
from ostorlab.agent.mixins import agent_persist_mixin as persist_mixin
from ostorlab.agent.mixins import agent_report_vulnerability_mixin as vuln_mixin
from ostorlab.runtimes import definitions as runtime_definitions
from rich import logging as rich_logging

logging.basicConfig(
    format='%(message)s',
    datefmt='[%X]',
    level='INFO',
    force=True,
    handlers=[rich_logging.RichHandler(rich_tracebacks=True)]
)
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')


def _run_snallygaster_command(domain: str) -> Any:
    command = ['snallygaster', domain, '-j', '-n']
    logger.info('running dnsReaper with command "%s"', ' '.join(command))
    with subprocess.Popen(command, stdout=subprocess.PIPE) as proc:
        proc.wait()
        logger.info('dnsReaper finished')
        output: Any = json.loads(proc.stdout.read())  # type: ignore
        return output


class SnallyGasterAgent(agent.Agent, vuln_mixin.AgentReportVulnMixin, persist_mixin.AgentPersistMixin):
    """Process the message and emit the findings"""

    def __init__(self, agent_definition: agent_definitions.AgentDefinition,
                 agent_settings: runtime_definitions.AgentSettings) -> None:
        agent.Agent.__init__(self, agent_definition, agent_settings)
        vuln_mixin.AgentReportVulnMixin.__init__(self)
        persist_mixin.AgentPersistMixin.__init__(self, agent_settings)

    def process(self, message: msg.Message) -> None:
        """Process only message of type v3.asset.domain_name"""
        domain_name: str = message.data.get('name', '')
        if domain_name is not None and self.set_add(b'agent_snallygaster', f'{domain_name}'):
            logger.info('processing domain name: %s', domain_name)
            findings = _run_snallygaster_command(domain_name)
            self._emit_findings(findings)

    def _emit_findings(self, findings: List[Dict[Any, Any]]) -> None:
        """Emit findings as a vulnerability"""
        for finding in findings:
            technical_detail = f"""```{finding}```"""
            self.report_vulnerability(entry=kb.KB.WEB_GENERIC,
                                      technical_detail=technical_detail,
                                      risk_rating=vuln_mixin.RiskRating.INFO)


if __name__ == '__main__':
    logger.info('starting agent dnsReaper ...')
    SnallyGasterAgent.main()
