from dataclasses import dataclass, asdict
from typing import Dict, Any

@dataclass
class ProbeResult:
    name: str
    passed: bool
    score: float
    prompt: str
    response: str
    reason: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
