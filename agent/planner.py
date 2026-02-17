from openai import OpenAI
from config import DEEPSEEK_API_KEY, DEEPSEEK_MODEL

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)

class Planner:

    def decide(self, goal, memory):

        system_prompt = '''
You are a planning agent.
Return ONLY JSON with:
{
  "action": ""
}
Possible actions:
classify_document
extract_fields
validate_fields
generate_decision
finish
'''

        response = client.chat.completions.create(
            model=DEEPSEEK_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Goal:{goal}\nMemory:{memory}"}
            ],
            temperature=0
        )

        return eval(response.choices[0].message.content)