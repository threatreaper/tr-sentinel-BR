from .prompt_injection import PROBE as prompt_injection
from .secret_leakage import PROBE as secret_leakage
from .instructions_leakage import PROBE as instructions_leakage
from .role_confusion import PROBE as role_confusion
from .jailbreaks import PROBE as jailbreaks
from .data_exfiltration import PROBE as data_exfiltration

ALL_PROBES = {
    'prompt_injection': prompt_injection,
    'secret_leakage': secret_leakage,
    'instructions_leakage': instructions_leakage,
    'role_confusion': role_confusion,
    'jailbreaks': jailbreaks,
    'data_exfiltration': data_exfiltration,
}
