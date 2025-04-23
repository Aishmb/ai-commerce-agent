from fastapi import APIRouter
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

router = APIRouter()

class QandARequest(BaseModel):
    question: str

class QandAResponse(BaseModel):
    answer: str

def get_answer_from_gpt(question: str) -> str:
    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" model
            prompt=question,  # Pass the question directly into the prompt
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)  # Return the error message if any error occurs

@router.post("/qa", response_model=QandAResponse)
async def qa_endpoint(request: QandARequest):
    answer = get_answer_from_gpt(request.question)
    print(f"Answer: {answer}")  # This will print the answer in your console logs
    return QandAResponse(answer=answer)
