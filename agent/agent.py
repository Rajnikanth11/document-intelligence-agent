import json
from agent.planner import Planner
from agent.tools import Tools
from agent.memory import Memory

class DocumentAgent:

    def __init__(self, schema_path: str):
        self.planner = Planner()
        self.tools = Tools()
        self.memory = Memory()

        with open(schema_path) as f:
            self.schema = json.load(f)

    def run(self, document_text: str):
        self.memory.save("document_text", document_text)
        goal = "Decide if document is ready for processing"

        while True:
            plan = self.planner.decide(goal, self.memory.dump())
            action = plan.get("action")

            if action == "classify_document":
                doc_type = self.tools.classify_document(document_text)
                self.memory.save("document_type", doc_type)

            elif action == "extract_fields":
                fields = self.tools.extract_fields(
                    document_text,
                    self.schema["fields"]
                )
                self.memory.save("extracted_fields", fields)

            elif action == "validate_fields":
                results = self.tools.validate_fields(
                    self.memory.get("extracted_fields"),
                    self.schema["rules"]
                )
                self.memory.save("validation_results", results)

            elif action == "generate_decision":
                decision = self.tools.generate_decision(
                    self.memory.get("validation_results")
                )
                self.memory.save("final_decision", decision)

            elif action == "finish":
                break

        return self.memory.dump()