from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class EvalResult:
    passed: bool
    score: float
    reason: str

def keyword_guardrail(text: str, *, must_not_contain: Optional[list[str]] = None, must_contain: Optional[list[str]] = None) -> EvalResult:
    text_l = (text or "").lower()
    reasons = []
    if must_not_contain:
        for k in must_not_contain:
            if k.lower() in text_l:
                reasons.append(f"found forbidden keyword: '{k}'")
    if must_contain:
        for k in must_contain:
            if k.lower() not in text_l:
                reasons.append(f"missing required keyword: '{k}'")
    passed = len([r for r in reasons if r.startswith("found forbidden")]) == 0
    score = 1.0 if passed and (not reasons or all(r.startswith("missing") for r in reasons)) else 0.0
    return EvalResult(passed=passed, score=score, reason="; ".join(reasons) or ("ok" if passed else "failed"))
