import re
import json
from llm.ollama_client import query_ollama

class Tools:

    def classify_document(self, text: str) -> str:
        if "policy" in text.lower():
            return "Insurance Submission"
        return "Unknown"

    def extract_fields(self, text: str, schema: dict) -> dict:
        extracted = {}
        for field in schema.keys():
            pattern = rf"{field}[:\-]\s*(.+)"
            match = re.search(pattern, text, re.IGNORECASE)
            extracted[field] = match.group(1).strip() if match else None
        return extracted

    def validate_fields(self, fields: dict, rules: dict) -> dict:
        if not fields:
            return {field: "MISSING" for field in rules}
        results = {}
        for field, rule in rules.items():
            value = fields.get(field)

            if rule.get("required") and not value:
                results[field] = "MISSING"
                continue

            if value and "max" in rule:
                try:
                    if float(value) > rule["max"]:
                        results[field] = "EXCEEDS_LIMIT"
                        continue
                except ValueError:
                    results[field] = "INVALID_NUMBER"

            results[field] = "OK"

        return results

    def extract_invoice_fields(self, text: str) -> dict:
        prompt = f"""
You are an invoice extraction engine.

Extract the following fields and return ONLY valid JSON.

Required fields:
- seller_name
- buyer_name
- invoice_number
- invoice_date
- total_amount
- amount_due
- currency

Convert numbers properly and use ISO date format (YYYY-MM-DD).

Document:
{text}
"""
        response = query_ollama(prompt)

        match = re.search(r"\{.*\}", response, re.DOTALL)
        if match:
            return json.loads(match.group())
        else:
            raise ValueError("No valid JSON found in Ollama response")

    def generate_decision(self, validation_results: dict) -> dict:
        if not validation_results:
            return {"decision": "REVIEW_REQUIRED", "reasons": ["validation_not_run"]}
        failed = [k for k, v in validation_results.items() if v != "OK"]

        if failed:
            return {"decision": "REVIEW_REQUIRED", "reasons": failed}

        return {"decision": "APPROVED", "reasons": []}