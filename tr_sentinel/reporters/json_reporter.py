import json

def to_json(report: dict) -> str:
    return json.dumps(report, indent=2)
