# model/admin.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db

AdminRouter = APIRouter(tags=["Admin"])

@AdminRouter.get("/Admin", response_model=list)
async def read_Admin(
    db=Depends(get_db)
):
    query= "SELECT Admin_ID,ID, Lab_Assigned, Name FROM admin"
    db[0].execute(query)
    Admin = [{ "Admin_ID": Admin[0], "ID": Admin[1], "Lab_Assigned": Admin[2], "Name": Admin[3]} for Admin in db[0].fetchall()]
    return Admin

@AdminRouter.get("/Admin/{AdminID}", response_model=dict)
async def read_Item(
    ID: str,
    db=Depends(get_db)
):
    query = "SELECT Admin_ID, Lab_Assigned , Name FROM admin WHERE ID = %s"
    db[0].execute(query, (ID,))
    Admin = db[0].fetchone()
    
    if Admin:
        return{
        "Admin_ID": Admin[0],
        "Lab_Assigned": Admin[1],
        "Name": Admin[2],
        }
    raise HTTPException(status_code=404, detail="Admin not found")


