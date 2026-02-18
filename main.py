from fastapi import FastAPI
from database import engine, Base
from routes import user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Management API",
    description="API for managing users — Create, Get All, Get by ID",
    version="1.0.0"
)

app.include_router(user_routes.router)
