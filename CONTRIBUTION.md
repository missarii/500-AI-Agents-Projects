difficulty: intermediate    # beginner | intermediate | advanced
llm: gpt-4o-mini
entrypoint: agent.py
requirements: requirements.txt
```

---

## Naming & layout conventions
- Folder names: lowercase, hyphen-separated (e.g., multi-agent-pursuit).
- Place one logical project per folder.
- Keep demos and notebooks near the code: demo.ipynb and run_demo.py in the project root.
- Avoid committing large binaries. Use .gitattributes or .gitignore to keep repository clean.

---

## Reproducibility & experiments
- Include seed values, environment variables, and exact dependency versions.
- Provide a minimal run command and expected output sample.
- For stochastic experiments, include evaluation scripts and deterministic seeds or checkpoints.
- If results require large compute or private data, include a small reproducible “toy” example that demonstrates the same pipeline on tiny inputs.

---

## Models, datasets & large files policy
- Don’t add large datasets or model checkpoints directly. Instead:
  - Provide a download script (download.sh / download.py) that fetches artifacts from a stable host (Hugging Face, S3, Zenodo).
  - Document the expected location/path after download.
- Clearly state dataset licenses, attribution, and any usage restrictions.
- When linking to external model weights provide their license and any fine-tuning provenance.

---

## Code style, documentation & tests
- Python: follow PEP 8, add a linter config (.flake8, pyproject.toml with [tool.black] or similar).
- JS/TS: provide ESLint/Prettier configs where relevant.
- Document complex algorithms with short docstrings and references.
- Add unit or integration tests when possible. Include a lightweight smoke test that CI can run quickly.

---

## Evaluation & metrics
- Include an evaluation script that produces metrics (accuracy, reward, latency).
- State measurement conditions (hardware, seeds).
- Where applicable, include latency and memory cost alongside performance metrics.

---

## CI / GitHub Actions recommendations
- If adding workflows, put them under .github/workflows and ensure expensive jobs are optional or use small inputs.
- Recommended checks: lint, unit tests, smoke demos. Heavy training jobs should be omitted or gated/opt-in.

