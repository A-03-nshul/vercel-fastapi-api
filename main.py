from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load data once when server starts
try:
    with open("data.json") as f:
        student_data = json.load(f)
except FileNotFoundError:
    # Dummy data if data.json not found
    student_data = [
        {"name": "quRZ", "marks": 85},
        {"name": "4Uy", "marks": 92},
        {"name": "another_student", "marks": 78},
    ]
    print("data.json not found. Using dummy data.")

@app.get("/api")
def get_marks(name: list[str] = []):
    # Map names to marks
    name_to_marks = {entry["name"]: entry["marks"] for entry in student_data}
    # Get marks for each name in order, None if not found
    marks = [name_to_marks.get(n) for n in name]
    return {"marks": name}
