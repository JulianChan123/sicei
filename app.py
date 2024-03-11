from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    id: Optional[int] = None
    matricula: str
    nombre: str

students = []

@app.get("/alumnos")
def getAllStudents():
    return students

@app.post("/alumnos")
def createStudent(student: Student):
    
    student.id = students.__len__()
    students.append(student.dict())
    return student

@app.get("/alumnos/{student_id}")
def getStudent(student_id: int):
    return students[student_id]

@app.put("/alumnos/{student_id}")
def updateStudent(student_id: int, student: Student):
    students[student_id] = student
    return student

@app.delete("/alumnos/{student_id}")   
def deleteStudent(student_id: int):
    students.pop(student_id)
    return students