from fastapi import FastAPI
from routes.event_routes import router as event_router
from routes.attendee_routes import router as attendee_router
from database import engine, Base

#Base.metadata.create_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(event_router)
app.include_router(attendee_router)
