from fastapi import FastAPI
from app.schemas import ResumeRequest, ResumeResponse
from app.inference import extract_entities


app = FastAPI(
    title="Resume Entity Extraction API",
    description="BERT-based NER service for extracting work experience entities",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/extract-entities", response_model=ResumeResponse)
def extract_resume_entities(request: ResumeRequest):
    entities = extract_entities(request.text)
    return {"entities": entities}
