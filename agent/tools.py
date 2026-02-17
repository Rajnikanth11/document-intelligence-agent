import re

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

    def generate_decision(self, validation_results: dict) -> dict:
        failed = [k for k, v in validation_results.items() if v != "OK"]

        if failed:
            return {"decision": "REVIEW_REQUIRED", "reasons": failed}

        return {"decision": "APPROVED", "reasons": []}