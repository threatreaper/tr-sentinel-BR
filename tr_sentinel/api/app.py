from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Dict, Any
import os

from tr_sentinel.orchestrator.runner import run_suite
from tr_sentinel.agents.openai_agent import get_agent

app = FastAPI(title="TR-Sentinel API", version="0.1.0")

allowed = os.getenv("TRS_ALLOWED_ORIGINS", "*")
origins = [o.strip() for o in allowed.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AgentCfg(BaseModel):
    type: Literal["simple", "openai"] = "simple"
    model: Optional[str] = "gpt-4o-mini"

class RunBody(BaseModel):
    agent: AgentCfg = Field(default_factory=AgentCfg)
    prompts: List[str] = []
    probes: Optional[List[str]] = None
    llm_eval: bool = False

@app.get("/healthz")
def healthz():
    return {"ok": True}

@app.post("/v1/run")
def run(body: RunBody) -> Dict[str, Any]:
    ag = get_agent(agent_type=body.agent.type, model=body.agent.model or "gpt-4o-mini")
    report = run_suite(agent=ag, prompts=body.prompts, only=body.probes)
    return report
