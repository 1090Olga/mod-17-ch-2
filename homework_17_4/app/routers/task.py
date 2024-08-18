from fastapi import APIRouter, Depends, status, HTTPException, Path
from slugify import slugify
from sqlalchemy.orm import Session
from typing import Annotated
from sqlalchemy import insert, select, update

from app.backend.db_depends import get_db
from app.schemas import CreateTask, UpdateTask
from app.models import *


router = APIRouter(prefix="/task", tags=["task"])

@router.get('/')
async def get_aii_tasks():
    pass

@router.get('/task_id')
async def get_task_by_id():
    pass

@router.post("/create")
async def create_task():
    pass

@router.put("/update")
async def update_task():
    pass

@router.delete("/delete")
async def delete_task():
    pass


