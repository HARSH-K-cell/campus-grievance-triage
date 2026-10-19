from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Project 20: Agentic Triage Assistant",
    description="Backend server for automated campus complaint triage and vector deduplication.",
    version="1.0"
)


class TicketRequest(BaseModel):
    ticket_id: str
    text: str

@app.get("/")
def read_root():
    return {
        "status": "online",
        "project": "Project 20: Agentic Triage Assistant",
        "team": "LOGIC LABS"
    }

@app.post("/submit-ticket")
def submit_ticket(ticket: TicketRequest):
    """
    Main endpoint where incoming tickets arrive.
    Integration point for AI Triage, FAISS Deduplication, and Safety Bypass modules.
    """
    
    # TODO: Member 4 will plug in Emergency Safety Bypass here
    # TODO: Member 2 will plug in AI Triage (Category & Urgency) here
    # TODO: Member 3 will plug in FAISS Vector Deduplication here

    return {
        "status": "received",
        "ticket_id": ticket.ticket_id,
        "content": ticket.text,
        "message": "Backend server is running successfully! Waiting for team module integration."
    }
