from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List, Dict, Any

@dataclass
class Agent:
    def reply(self, user_message: str, system_prompt: Optional[str] = None) -> str:
        raise NotImplementedError

class SimpleEchoAgent(Agent):
    """Deterministic, offline agent for tests and CI."""
    def reply(self, user_message: str, system_prompt: Optional[str] = None) -> str:
        sp = f"[SYSTEM:{system_prompt}]" if system_prompt else ""
        return f"{sp} ECHO: {user_message}"

class OpenAIChatAgent(Agent):
    def __init__(self, model: str = "gpt-4o-mini"):
        try:
            from openai import OpenAI
        except Exception as e:
            raise RuntimeError("Install extra: pip install 'tr-sentinel[openai]'") from e
        self._client = OpenAI()
        self.model = model

    def reply(self, user_message: str, system_prompt: Optional[str] = None) -> str:
        msgs = []
        if system_prompt:
            msgs.append({"role": "system", "content": system_prompt})
        msgs.append({"role": "user", "content": user_message})
        resp = self._client.chat.completions.create(model=self.model, messages=msgs)
        return resp.choices[0].message.content or ""

def get_agent(agent_type: str = "simple", model: str = "gpt-4o-mini") -> Agent:
    if agent_type == "openai":
        return OpenAIChatAgent(model=model)
    return SimpleEchoAgent()
