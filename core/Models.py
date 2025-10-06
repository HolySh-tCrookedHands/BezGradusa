from pydantic import BaseModel

class AuthReg(BaseModel):
    login: str 
    password: str 
    email: str

class AuthLogin(BaseModel):
    login: str 
    password: str | int | float