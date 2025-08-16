from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Supercell Stat Tracker!"}