from pydantic import BaseModel


class HTTPBadRequest(BaseModel):
    error: str


class APISigninRequest(BaseModel):
    username: str
    password: str


class APISigninResponse(BaseModel):
    msg: str


class AccountLoggedinInfo(BaseModel):
    status: bool
    message: str
