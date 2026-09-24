import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI(title="LegalEase API")

class DocumentRequest(BaseModel):
    doc_type: str
    details: str

@app.post("/generate-doc")
async def generate_document(req: DocumentRequest):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Create a formal legal document of type '{req.doc_type}'. Details provided: {req.details}. Ensure proper legal structure and clauses."
        response = model.generate_content(prompt)
        return {"document": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
