import json
from llm.ollama_client import query_ollama


class Planner:

    def decide(self, goal: str, memory: dict) -> dict:

        prompt = f"""
You are a planning agent.
Return ONLY valid JSON with this exact structure:
{{
  "action": ""
}}

Possible actions:
- classify_document
- extract_fields
- validate_fields
- generate_decision
- finish

Goal: {goal}
Memory: {json.dumps(memory)}
"""

        result = query_ollama(prompt)

        # Strip markdown code fences if present (e.g. ```json ... ```)
        result = result.strip()
        if result.startswith("```"):
            result = result.split("```")[1]
            if result.startswith("json"):
                result = result[4:]

        return json.loads(result.strip())
