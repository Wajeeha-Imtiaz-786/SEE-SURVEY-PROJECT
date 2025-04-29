import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Update database credentials to use environment variables
DB_USERNAME = os.getenv("DB_USERNAME", "survey_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "Islamabad123#")
DB_HOST = os.getenv("DB_HOST", "localhost")
# Ensure DB_PORT is converted to an integer with a valid default
DB_PORT = int(os.getenv("DB_PORT", 3306))  # Default to 3306 for MySQL
DB_NAME = os.getenv("DB_NAME", "see_survey_db")

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Debugging: Print the database connection details
print(f"DB_PORT: {DB_PORT}")
print(f"DATABASE_URL: {DATABASE_URL}")

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model for ORM
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()