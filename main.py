from typing import Optional, Annotated

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Depends

app = FastAPI()

class STasksAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STasksAdd):
    id: int

tasks = []

# decorators
@app.post('/tasks')
async def add_tasks(
        task: Annotated[STasksAdd, Depends()]
):
    tasks.append(task)
    return {'ok': True}


# @app.get('/task')
# def get_task():
#     task = Task(name='Write this is video')
#     return {'data':task}
