from fastapi import FastAPI
from auth.routers import router as auth_router
from posts.routers import router as posts_router
from database.database import engine
from database import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(posts_router)
