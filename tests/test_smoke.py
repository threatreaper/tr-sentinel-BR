from tr_sentinel.agents.openai_agent import get_agent
from tr_sentinel.orchestrator.runner import run_suite

def test_smoke():
    agent = get_agent("simple")
    r = run_suite(agent, prompts=["hi"], only=["prompt_injection"]
    )
    assert r["summary"]["total"] == 1
