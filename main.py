from ingestion.pdf_loader import pdf_to_text
from agent.agent import DocumentAgent

if __name__ == "__main__":

    document_text = pdf_to_text("C:\\Users\\kausa\\OneDrive\\Documents\\personal\\document-agent\\AL-2500003297.pdf")

    agent = DocumentAgent("schemas/insurance.json")
    result = agent.run(document_text)

    print(result)