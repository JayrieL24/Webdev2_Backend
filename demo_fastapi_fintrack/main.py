# main.py
from fastapi import FastAPI
from model.users import UsersRouter
from model.categories import CategoriesRouter
from model.expenses import ExpensesRouter
from model.students import StudentsRouter
from model.personnel import PersonnelRouter
from model.items import ItemsRouter
from model.admin import AdminRouter
app = FastAPI()

# Include CRUD routes from modules
app.include_router(UsersRouter, prefix="/api")
app.include_router(CategoriesRouter, prefix="/api")
app.include_router(ExpensesRouter, prefix="/api")
app.include_router(StudentsRouter, prefix="/api")
app.include_router(PersonnelRouter, prefix="/api")
app.include_router(ItemsRouter, prefix="/api")
app.include_router(AdminRouter, prefix="/api")