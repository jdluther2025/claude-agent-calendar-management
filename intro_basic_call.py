import os

import anthropic

client = anthropic.Anthropic()

# Model is read from the MODEL environment variable.
# Set it in your shell before running:
#
#   export MODEL="claude-haiku-4-5-20251001"   # fast, cost-efficient
#   export MODEL="claude-sonnet-4-6"            # balanced, strong reasoning
#   export MODEL="claude-opus-4-6"              # most capable (default — matches tutorial)
#
MODEL = os.environ.get("MODEL", "claude-opus-4-6")

message = client.messages.create(
    model=MODEL,
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "I need to schedule a 30-minute sync with alice@example.com and bob@example.com next Monday at 10am. What information do I need to create this calendar event?",
        }
    ],
)

print(message.content[0].text)
