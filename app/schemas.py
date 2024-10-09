from pydantic import BaseModel


class ErrorLogIn(BaseModel):
    message: str
    traceback: str
