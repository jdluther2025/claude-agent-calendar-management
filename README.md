# Claude Agent — Calendar Management

Companion code for the tutorial:

**[🗓️ Claude Tutorial — Build a Tool-Using AI Agent: Calendar Management](https://medium.com/ai-ml-human-training-coaching/%EF%B8%8F-claude-tutorial-build-a-tool-using-ai-agent-calendar-management-45aae4c11d0b)**

The Official Practice Version — A guided walkthrough from a single tool call to a production-ready agentic loop.

---

## What's in This Repo

| File | Ring | What It Teaches |
|------|------|-----------------|
| `intro_basic_call.py` | Intro | First Claude API call — no tools |
| `ring1_tool_use.py` | Ring 1 | Single tool, single turn |
| `ring2_agentic_loop.py` | Ring 2 | The agentic loop — run until done |
| `ring3_multiple_tools.py` | Ring 3 | Multiple tools, parallel calls |
| `ring4_error_handling.py` | Ring 4 | Tools fail — handle it gracefully |
| `ring5_tool_runner.py` | Ring 5 | SDK abstraction — production-ready |

Each file is standalone. Run any ring independently.

> **Note:** `create_calendar_event` and `list_calendar_events` return hardcoded responses — real calendar connectivity is coming in the next post.

---

## Setup

```bash
# Clone the repo
git clone https://github.com/jdluther2025/claude-agent-calendar-management.git
cd claude-agent-calendar-management

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the SDK
pip install anthropic

# Set your API key
export ANTHROPIC_API_KEY=sk-ant-...

# Set the model (default: Haiku)
export MODEL="claude-haiku-4-5-20251001"
```

---

## Run the Rings

```bash
python3 intro_basic_call.py
python3 ring1_tool_use.py
python3 ring2_agentic_loop.py
python3 ring3_multiple_tools.py
python3 ring4_error_handling.py
python3 ring5_tool_runner.py
```

---

## Model Options

All scripts read the model from the `MODEL` environment variable:

```bash
export MODEL="claude-haiku-4-5-20251001"   # fast, cost-efficient (default)
export MODEL="claude-sonnet-4-6"            # balanced, strong reasoning
export MODEL="claude-opus-4-6"              # most capable
```
