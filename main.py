from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data once when server starts
with open("data.json") as f:
    student_data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = []):
    name_to_marks = {entry["name"]: entry["marks"] for entry in student_data}
    marks = [name_to_marks.get(n, None) for n in name]
    return {"marks": marks}
