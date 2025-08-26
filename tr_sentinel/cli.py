from typing import Optional, List
import json
import typer
from rich.console import Console
from tr_sentinel.orchestrator.runner import run_suite, list_probe_names
from tr_sentinel.agents.openai_agent import get_agent

console = Console()
app = typer.Typer(add_completion=False, help="TR-Sentinel CLI")

@app.command()
def probes():
    """List available probes."""
    for name in list_probe_names():
        console.print(f"- {name}")

@app.command()
def run(
    agent: str = typer.Option("simple", help="Agent type: simple | openai"),
    model: str = typer.Option("gpt-4o-mini", help="OpenAI model if agent=openai"),
    prompts: List[str] = typer.Option([], help="One or more prompts to seed context."),
    probes: List[str] = typer.Option([], help="Subset of probes to run (default: all)."),
    json_out: Optional[str] = typer.Option(None, "--json", help="Write JSON report to file"),
):
    ag = get_agent(agent_type=agent, model=model)
    results = run_suite(agent=ag, prompts=prompts, only=probes or None)
    if json_out:
        with open(json_out, "w") as f:
            json.dump(results, f, indent=2)
        console.print(f"[green]Wrote JSON report to[/] {json_out}")
    else:
        from tr_sentinel.reporters.console import print_console_report
        print_console_report(results)

@app.command()
def api(host: str = "127.0.0.1", port: int = 8000):
    import uvicorn
    uvicorn.run("tr_sentinel.api.app:app", host=host, port=port, reload=False)

if __name__ == "__main__":
    app()
