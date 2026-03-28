import os
from dotenv import load_dotenv

# Load .env file at the earliest possible stage
load_dotenv()

class Config:
    # Use environment variable, with a fallback for local development stability
    SECRET_KEY = os.getenv("SECRET_KEY", "jobready-dev-secret-key-2026")
    
    # Use PostgreSQL in production (Render provides DATABASE_URL)
    # Default to local SQLite for development
    database_url = os.getenv("DATABASE_URL")
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
        
    SQLALCHEMY_DATABASE_URI = database_url or "sqlite:///jobready.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False