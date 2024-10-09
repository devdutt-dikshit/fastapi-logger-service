from sqlalchemy import Column, String, Integer
from .database import Base


class ErrorLog(Base):
    __tablename__ = "error_logs"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    traceback = Column(String)
