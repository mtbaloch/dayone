from fastapi import FastAPI, HTTPException, Query
from typing import Optional, List
from pydantic import BaseModel, field_validator
app = FastAPI(
    title="dayone",
    description="learning basics of fastapi",
    version="0.0.1"
    )

# first api route

# Get is http method that is used to get data from server and send it
# to the client
# with get, we can use path parameters and query parameters

@app.get("/")
async def root():
    return {"status":True, "message":"Api is up"}

# Post is used to create a new resouce on the server in database
# Post request must have body with data


class Users(BaseModel):
    user_name: str
    user_email: str
    user_password: str
    
    @field_validator("user_email")
    def validate_email(cls, value):
        if not value.endswith("@tahir.com"):
            raise ValueError("Email must belong to the @tahir.com domain.")
        return value
    

@app.post("/users")
async def create_user(
    user_name: Optional[str] = Query(None),
    user_email: Optional[str] = Query(None),
    user_password: Optional[str] = Query(None)
):
    # data validation
    # Check if required fields are missing
    if not user_name or not user_email or not user_password:
        return {"message": "Please fill all the required fields."}
    
    # Return success message
    return {"status": True, "message": "User created successfully."}

@app.post("/users/create")
async def create_user(
    user_data: Users
):
    user = user_data.model_dump()
    # data validation
    # Check if required fields are missing
    if not user_data:
        return {"message": "Please fill all the required fields."}

    print(user_data)
    # Return success message
    return {"status": True, "message": "User created successfully.", "newUser": {"user_name":user["user_name"]}}

users =[
    {"user_name": "user1", "user_password": "password1", "user_email": "user1@example.com"},
    {"user_name": "user2", "user_password": "password2", "user_email": "user2@example.com"},
    {"user_name": "user3", "user_password": "password3", "user_email": "user3@example.com"},
    {"user_name": "user4", "user_password": "password4", "user_email": "user4@example.com"},
    {"user_name": "user5", "user_password": "password5", "user_email": "user5@example.com"},
    {"user_name": "user6", "user_password": "password6", "user_email": "user6@example.com"},
    {"user_name": "user7", "user_password": "password7", "user_email": "user7@example.com"},
    {"user_name": "user8", "user_password": "password8", "user_email": "user8@example.com"},
    {"user_name": "user9", "user_password": "password9", "user_email": "user9@example.com"},
    {"user_name": "user10", "user_password": "password10", "user_email": "user10@example.com"}
]


@app.get("/users")
async def users_data():
    return {"users":users}


@app.get("/users/{user_name}")
async def get_single_user(user_name: str):
    
    if user_name is None:
        return {"message":"user name is required."}
        
    for user in users:
        if user["user_name"] == user_name:
            return {"users": {"user_name": user["user_name"], "user_email":user["user_email"]}}
        
    raise HTTPException(status_code=404, detail="User not found")

