from fastapi import FastAPI
from .router import posts
from .router import users,auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)



@app.get("/")
async def read_root():
    return {"username":settings.database_username}
