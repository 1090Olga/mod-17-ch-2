
from fastapi import APIRouter


router = APIRouter(prefix="/task", tags="task")

@router.get('/all_tasks')
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


