import os
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db.session import get_db

app = FastAPI()

@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    return {"status": "Successfully connected to Neon PostgreSQL!"}

@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI application!"}
