from fastapi import FastAPI
from routers import task
from routers import user
app = FastAPI()


@app.get("/")
async def welcome():
    return {"massage": "My shop"}

app.include_router(task.router)
app.include_router(user.router)