
from fastapi import FastAPI,HTTPException     #python imports FastAPI class
from pydantic import BaseModel

app = FastAPI()                 #python creates the application    

class User(BaseModel):
    id : int
    name : str
    age : int


# @app.get("/products")                   #If someone asked for "/", call the function home().
# def get_products(category = None):
#     return {"category": category}

users = []


@app.post("/users")
def create_user(user:User):
    users.append(user)

    return user

@app.get("/users")
def get_users():
    return users


@app.get("/health")
def health():
    return {"status": "ok"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return {"message": "user deleted"}
        
    raise HTTPException(status_code=404, detail= "no user found")