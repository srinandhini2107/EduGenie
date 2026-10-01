from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn

from summary_module import generate_summary
from explanation_module import generate_explanation
from qna import answer_question
from learning_path import generate_learning_path
from quiz_module import generate_quiz

app = FastAPI(title="EduGenie AI")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class TopicRequest(BaseModel):
    topic: str

class SummaryRequest(BaseModel):
    text: str

class QnaRequest(BaseModel):
    question: str
    context: str = ""

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/api/summary")
def api_summary(req: SummaryRequest):
    return {"result": generate_summary(req.text)}

@app.post("/api/explain")
def api_explain(req: TopicRequest):
    return {"result": generate_explanation(req.topic)}

@app.post("/api/qna")
def api_qna(req: QnaRequest):
    return {"result": answer_question(req.question, req.context)}

@app.post("/api/learning-path")
def api_learning_path(req: TopicRequest):
    return generate_learning_path(req.topic)

@app.post("/api/quiz")
def api_quiz(req: TopicRequest):
    return generate_quiz(req.topic)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)