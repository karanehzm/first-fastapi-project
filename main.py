
from fastapi import FastAPI, HTTPException, Depends    #python imports FastAPI class
from pydantic import BaseModel
from database import engine, get_db
import models


# models.Base.metadata.create_all(bind= engine)



app = FastAPI()                 # python creates the application    

class User(BaseModel):      # pydantic models for API to check the validity of the data types
    id : int
    name : str
    age : int



class UserUpdate(BaseModel):
    
    name : str | None = None
    age : int | None = None



class WorkspaceCreate(BaseModel):
    name: str
    owner_id: int 


# users = []                  # the users are in memory. if the server resetarts the users disappear.




@app.post("/users")         # because the user: is a pydantic model.
                            # FastAPI understands that the data should come from the request body.

def create_user(user:User, db = Depends(get_db)):
    new_user = models.User(
        id = user.id,
        name = user.name,
        age = user.age
    )

    db.add(new_user)
    db.commit()

    return new_user



@app.get("/users")
def get_users(db = Depends(get_db)):
    return db.query(models.User).all()



@app.get("/health")
def health():
    return {"status": "healthy"}



@app.get("/")
def home():
    return {"Message: API is running"}



@app.get("/users/{user_id}")
def get_users_id(user_id: int, db =Depends(get_db)):

    # for user in db.query(models.User).all():
    #     if user.id == user_id:
    #         return user

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code = 404, detail="user not found")
    
    return user




@app.delete("/users/{user_id}")
def delete_user(user_id: int, db = Depends(get_db)):

    # for user in users:
    #     if user.id == user_id:
    #         users.remove(user)
    #         return {"message": "user deleted"}

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"message": "user deleted"}
    

        
    raise HTTPException(status_code=404, detail= "no user found")



@app.put("/users/{user_id}")        # updates the user 
def update_user(user_id: int, updated_user: User, db = Depends(get_db)):
    # for user in users:
    #     if user.id == user_id:
    #         user.name = updated_user.name
    #         user.age = updated_user.age

    #         return user
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.name = updated_user.name
        user.age = updated_user.age
        db.commit()

        return {"message": "User is updated"}

        
    raise HTTPException(status_code = 404, detail = "user not found")



@app.patch("/users/{user_id}")
def partially_update_user(user_id: int, updated_user: UserUpdate, db = Depends(get_db)):
    # for user in users:
    #     if user.id == user_id:
    #         if updated_user.name is not None:
    #             user.name = updated_user.name
                
    #         if updated_user.age is not None:
    #             user.age = updated_user.age
    
    #         return user

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        if updated_user.name is not None:
            user.name = updated_user.name

        if updated_user.age is not None:
            user.age = updated_user.age

        db.commit()
        return {"message": "User partially updated"}
    
    raise HTTPException(status_code = 404, detail = "user not found")


@app.post("/workspaces")
def create_workspace(workspace: WorkspaceCreate, db = Depends(get_db)):

    new_workspace = models.Workspace(
        name = workspace.name,
        owner_id = workspace.owner_id
    )


    owner = db.query(models.User).filter(
        models.User.id == workspace.owner_id
    ).first()

    if owner is None:
        raise HTTPException(
            status_code = 404,
            detail = "owner not found"
        )
        
    db.add(new_workspace)
    db.commit()
    return new_workspace



@app.get("/workspaces/{workspace_id}")
def get_workspace(workspace_id: int , db = Depends(get_db)):

    res = db.query(models.Workspace).filter(models.Workspace.id == workspace_id).first()

    if res is None:
        raise HTTPException(status_code= 404,
                      detail = "workspace doesnt exist")
    return res


@app.get("/workspaces") #this one gets all the workspaces
def get_workspaces(db = Depends(get_db)):

    res = db.query(models.Workspace).all()

    if res is not None:
        return res
    
