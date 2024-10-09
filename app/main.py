from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from .database import init_db, SessionLocal
from .models import ErrorLog
from .schemas import ErrorLogIn
from .middleware import ip_whitelist_middleware

app = FastAPI()

init_db()

templates = Jinja2Templates(directory="app/templates")


app.middleware("http")(ip_whitelist_middleware)


@app.post("/log/")
async def log_error(error: ErrorLogIn):
    db = SessionLocal()
    error_log = ErrorLog(message=error.message, traceback=error.traceback)
    db.add(error_log)
    db.commit()
    db.refresh(error_log)
    db.close()
    return {"id": error_log.id, "message": "Error logged successfully!"}


@app.get("/logs/")
async def get_logs(request: Request):
    db = SessionLocal()
    logs = db.query(ErrorLog).all()
    db.close()
    return templates.TemplateResponse("logs.html", {"request": request, "logs": logs})
