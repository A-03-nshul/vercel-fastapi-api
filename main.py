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
try:
    with open("daa.json") as f:
        student_data = json.load(f)
except FileNotFoundError:
    # Create a dummy data if data.json is not found for demonstration
    student_data = [
        {"name": "quRZ", "marks": 85},
        {"name": "4Uy", "marks": 92},
        {"name": "another_student", "marks": 78},
    ]
    print("data.json not found. Using dummy data.")

app = FastAPI()

@app.get("/api")
def get_marks(name: list[str] = []):
    # Create a dictionary mapping names to marks for quick lookup
    name_to_marks = {entry["name"]: entry["marks"] for entry in student_data}

    # Retrieve marks for each requested name
    # If a name is not found in student_data, None is returned
    marks = [name_to_marks.get(n, None) for n in name]

    # Return the marks in a dictionary
    return {"marks": marks}
