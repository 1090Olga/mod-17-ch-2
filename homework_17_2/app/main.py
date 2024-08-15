from fastapi import FastAPI
from homework_17_2.app.routers import task
from homework_17_2.app.routers import user
app = FastAPI()


@app.get("/")
async def welcome():
    return {"massage": "My shop"}

app.include_router(task.router)
app.include_router(user.router)

