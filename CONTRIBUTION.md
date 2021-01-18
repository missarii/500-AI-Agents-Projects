# Contributing to 500-AI-Agents-Projects

Welcome — this repository collects 500 AI agent projects, templates, demos, and integrations. Thank you for helping grow a practical, reproducible, and responsible catalog of agent work. This document is tuned to the AI-agent focus of the project: reproducibility, model/data hygiene, evaluation, and safety.

Quick summary
- Add small, runnable, well-documented agent examples and templates.
- Prefer reproducible demos and small checkpoints or external download scripts.
- Follow the folder schema and metadata so projects are discoverable and automatable.
- Pay attention to license, data provenance, and ethical/safety notes.

---

## What to contribute
- New agent projects (single- or multi-agent; code, notebooks, or demos).
- Templates/boilerplates for agent types (reactive, planning-based, learning agents, RL, LLM-based, etc.).
- Integrations (environments, simulators, observability / logging tools).
- Shared tooling (evaluation harnesses, metrics, benchmark suites, dataset loaders).
- Docs, reproducible experiments, visualization utilities, or lightweight datasets (or links to them).

If your contribution is large (new category, many projects, major refactor) please open an issue first to coordinate placement and naming.

---

## Project folder requirements (must-have)
Each agent project added must include the following at the top level of its folder:

Agents live in `agents/NN-agent-name/` where `NN` is the next free number. Copy the
layout of an existing agent — `agents/01-web-research-agent/` is the reference. Exactly
five files, nothing more:

- `README.md` — what it does, quick start with exact commands, sample output, and rough runtime.
- `agent.py` — the runnable entrypoint. Must run end-to-end in under 10 minutes.
  A notebook is fine instead if the demo is genuinely better that way.
- `requirements.txt` — pin your versions. `pyproject.toml` or `environment.yml` also fine.
- `.env.example` — every env var the agent needs, with placeholder values. Never a real key.
- `metadata.yaml` — see the schema below.

Everything here is MIT under the repository root `LICENSE`. If your agent pulls in code,
models, or data under a different licence, say so in your README and link the source.

Large models and datasets don't belong in the repo. Host them externally (Hugging Face,
S3, Zenodo) and add a download script.

metadata.yaml schema
```yaml
title: web-research-agent
description: Searches the web for a topic and synthesizes a structured research report
author: your-github-username
language: python
framework: langgraph        # langgraph | crewai | autogen | agno | llamaindex | other
tags: [research, web-search, rag, langgraph]
industry: general
