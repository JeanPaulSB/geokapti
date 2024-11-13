from fastapi import FastAPI
from .core.database import  init_db
app = FastAPI()


connection = init_db()

print(connection)
@app.get("/")
async def root():
    return {"message": "Hello World"}
