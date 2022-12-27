from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/users")
def read_users():
    return {"message": "read_users()"}


@app.post("/users")
def create_user():
    return {"message": "create_user()"}


@app.delete("/users/{id}")
def delete_user(id: int):
    return {"message": f"read_users(){id}"}


@app.post("/users/{id}")
def read_users(id: int):
    return {"message": f"read_users(){id}"}

if __name__ == '__main__':
    uvicorn.run("task_2:app", host="127.0.0.1", port=5000, log_level="info")