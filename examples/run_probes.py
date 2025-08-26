from tr_sentinel.agents.openai_agent import get_agent
from tr_sentinel.orchestrator.runner import run_suite
from tr_sentinel.reporters.console import print_console_report

if __name__ == "__main__":
    agent = get_agent("simple")
    report = run_suite(agent, prompts=["Hello!"])
    print_console_report(report)
