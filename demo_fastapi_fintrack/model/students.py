# model/students.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db

StudentsRouter = APIRouter(tags=["Students"])


@StudentsRouter.get("/students/", response_model=list)
async def read_students(
    db=Depends(get_db)
):
    query = "SELECT ID, Name, Course FROM student"
    db[0].execute(query)
    students = [{"ID": students[0], "Name": students[1], "Course": students[2]} for students in db[0].fetchall()]
    return students

@StudentsRouter.get("/students/{ID}",response_model=dict)
async def read_student(
    ID: str ,
    db=Depends(get_db)
):

    query = "SELECT ID, Name, Course FROM student WHERE ID = %s"
    db[0].execute(query, (ID,))
    student = db[0].fetchone()
    
    if student:
        return{
            "ID": student[0],
            "Name": student[1],
            "Course": student[2],
        }
    raise HTTPException(status_code=404, detail="Student not found")
    

@StudentsRouter.post("/students/", response_model=dict)
async def create_student(
     ID: str = Form(...),
     Name: str = Form(...),
     Course: str = Form(...),
    db=Depends(get_db)
):
    query = "INSERT INTO student (ID, Name, Course) VALUES (%s, %s, %s)"
    db[0].execute(query,(ID,Name,Course))
    db[1].commit()
    
    return {
                    "ID": student[0],
                    "Name": student[1],
                    "Course": student[2],
    }