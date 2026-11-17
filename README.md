# Applied AI Projects

Hands-on LLM projects from my personal AI engineering learning journey: prompting, RAG, agents and evals.

## 01 - LLM Basics
A simple script that calls the Claude API, plus experiments with temperature and max tokens.

**What I found**
- Temperature 0 gave the same answer every time; temperature 1 added variety.
- A low max_tokens cuts replies off mid-sentence (stop reason: `max_tokens`).
- Newer Claude models no longer accept a custom temperature (API change, Oct 2026), so I used the older API version for these experiments.

**Run it**
1. `pip install anthropic python-dotenv`
2. Add `ANTHROPIC_API_KEY=...` to a `.env` file
3. `python 01-llm-basics/experiments.py`