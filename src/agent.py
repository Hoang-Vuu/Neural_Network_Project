import json
import os
try:
    from google.colab import userdata
except ImportError:
    userdata = None
from groq import Groq

from tools import TOOL_SCHEMAS, TOOL_REGISTRY

MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")

SYSTEM_PROMPT = """
You plan outdoor trips using the attraction database and weather forecast.

Use real attraction records and forecast results. Never invent data.

A suitable day must have BOTH:
- Maximum precipitation probability below 30%.
- Maximum wind speed below 35 km/h.

If no forecast day meets both rules, state that clearly.
Explain the values used. Never claim missing weather data is suitable.
The database does not provide opening hours.
Keep the final answer short.
"""

def run_agent(user_request, max_iterations=5):
    api_key = os.getenv("GROQ_API_KEY") or (userdata.get("GROQ_API_KEY") if userdata else None)
    if not api_key:
        raise RuntimeError("Add GROQ_API_KEY in Colab Secrets.")

    client = Groq(api_key=api_key)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_request},
    ]
    trace = []

    for iteration in range(max_iterations):
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOL_SCHEMAS,
            tool_choice="auto",
            temperature=0.2,
            max_completion_tokens=300,
            parallel_tool_calls=False,
        )

        msg = response.choices[0].message
        calls = msg.tool_calls

        trace.append({
            "iteration": iteration + 1,
            "event": "model_response",
            "content": msg.content,
            "tool_calls": [
                {
                    "id": c.id,
                    "name": c.function.name,
                    "arguments": c.function.arguments,
                }
                for c in (calls or [])
            ],
        })

        if not calls:
            return {
                "answer": msg.content or "",
                "trace": trace,
            }

        messages.append(msg.model_dump(exclude_none=True))

        for call in calls:
            name = call.function.name

            if name not in TOOL_REGISTRY:
                result = {"error": f"Tool not approved: {name}"}
            else:
                try:
                    args = json.loads(call.function.arguments)
                    result = TOOL_REGISTRY[name].invoke(args)
                except Exception as exc:
                    result = {"error": f"{type(exc).__name__}: {exc}"}

            trace.append({
                "iteration": iteration + 1,
                "event": "tool_result",
                "tool": name,
                "result": result,
            })

            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "name": name,
                "content": json.dumps(
                    result, ensure_ascii=False, default=str
                ),
            })

    return {
        "answer": "Tool-call limit reached. Inspect the trace and retry.",
        "trace": trace,
    }
