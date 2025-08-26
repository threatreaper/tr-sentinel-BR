from rich.console import Console
from rich.table import Table

def print_console_report(report: dict):
    console = Console()
    s = report["summary"]
    console.rule("TR-Sentinel Report")
    console.print(f"Total: {s['total']}  Passed: {s['passed']}  Failed: {s['failed']}  Score: {s['score']}")

    table = Table(title="Probe Results")
    table.add_column("Probe")
    table.add_column("Passed")
    table.add_column("Score")
    table.add_column("Reason")
    for r in report["results"]:
        table.add_row(r["name"], "✅" if r["passed"] else "❌", str(r["score"]), r.get("reason", ""))
    console.print(table)
