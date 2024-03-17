# model/personnel.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db

PersonnelRouter = APIRouter(tags=["Personnel"])

@PersonnelRouter.get("/personnel", response_model=list)
async def read_personnels(
    db=Depends(get_db)
):
    query= "SELECT ID, Department, Name FROM personnel"
    db[0].execute(query)
    personnels = [{"ID": personnels[0], "Department": personnels[1], "Name": personnels[2]} for personnels in db[0].fetchall()]
    return personnels

@PersonnelRouter.get("/personnel/{ID}", response_model=dict)
async def read_personnel(
    ID: str,
    db=Depends(get_db)
):
    query = "SELECT ID, Department, Name FROM personnel WHERE ID = %s"
    db[0].execute(query, (ID,))
    personnel = db[0].fetchone()
    
    if personnel:
        return{
            "ID": personnel[0],
            "Department": personnel[1],
            "Name": personnel[2],
        }
    raise HTTPException(status_code=404, detail="Personnel not found")

@PersonnelRouter.post("/personnel/", response_model=dict)
async def create_personnel(
     ID: str = Form(...),
     Department: str = Form(...),
     Name: str = Form(...),
    db=Depends(get_db)
):
    query = "INSERT INTO personnel (ID, Department, Name) VALUES (%s, %s, %s)"
    db[0].execute(query,(ID,Department,Name))
    db[1].commit()
    
    return {
                    "ID": personnel[0],
                    "Department": personnel[1],
                    "Name": personnel[2],
    }