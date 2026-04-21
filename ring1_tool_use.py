import json
import os

import anthropic

client = anthropic.Anthropic()

MODEL = os.environ.get("MODEL", "claude-haiku-4-5-20251001")

# Define one tool. The input_schema includes nested objects (recurrence),
# arrays (attendees), and optional fields — closer to real-world tools
# than a flat string argument.
tools = [
    {
        "name": "create_calendar_event",
        "description": "Create a calendar event with attendees and optional recurrence.",
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {"type": "string"},
                "start": {"type": "string", "format": "date-time"},
                "end": {"type": "string", "format": "date-time"},
                "attendees": {
                    "type": "array",
                    "items": {"type": "string", "format": "email"},
                },
                "recurrence": {
                    "type": "object",
                    "properties": {
                        "frequency": {"enum": ["daily", "weekly", "monthly"]},
                        "count": {"type": "integer", "minimum": 1},
                    },
                },
            },
            "required": ["title", "start", "end"],
        },
    }
]


# The function Claude will ask us to run
def create_calendar_event(title, start, end, attendees=None, recurrence=None):
    # Hardcoded result — in a real system this would call your calendar API
    return {"event_id": "evt_123", "status": "created", "title": title}


# Step 1 — send the first message with the tool available
response = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "auto", "disable_parallel_tool_use": True},
    messages=[
        {
            "role": "user",
            "content": "Schedule a 30-minute sync with alice@example.com and bob@example.com next Monday at 10am.",
        }
    ],
)

# Step 2 — Claude stopped to call a tool
print(f"Stop reason: {response.stop_reason}")

tool_use = next(block for block in response.content if block.type == "tool_use")
print(f"Tool: {tool_use.name}")
print(f"Input: {tool_use.input}")

# Step 3 — execute the function
result = create_calendar_event(**tool_use.input)
print(f"Result: {result}")

# Step 4 — send the result back
messages = [
    {
        "role": "user",
        "content": "Schedule a 30-minute sync with alice@example.com and bob@example.com next Monday at 10am.",
    },
    {"role": "assistant", "content": response.content},
    {
        "role": "user",
        "content": [
            {
                "type": "tool_result",
                "tool_use_id": tool_use.id,
                "content": json.dumps(result),
            }
        ],
    },
]

# Step 5 — get Claude's final answer
final_response = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    tools=tools,
    tool_choice={"type": "auto", "disable_parallel_tool_use": True},
    messages=messages,
)

print(f"Stop reason: {final_response.stop_reason}")
print("\n--- Claude's answer ---")
final_text = next(block for block in final_response.content if block.type == "text")
print(final_text.text)
