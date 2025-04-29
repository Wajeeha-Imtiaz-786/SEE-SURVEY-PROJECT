import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from database import Base, engine
from routers import user, project, role
from routers import site_location, survey_visit, site_information, site_access
from routers import site_session


# Initialize FastAPI
app = FastAPI(
    title="Site Survey Backend",
    description="API backend for managing site survey data",
    version="1.0.0"
)

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Serve static files (like HTML, JS, CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the signup HTML page
@app.get("/signup", response_class=FileResponse, tags=["Static Pages"])
def get_signup_page():
    """Serve the signup page located in the static directory."""
    return FileResponse("static/signup.html", media_type="text/html")

# Optional: root endpoint for API health check
@app.get("/", tags=["Health Check"])
def read_root():
    """Health check endpoint to verify the API is running."""
    return {"message": "Welcome to the Site Survey Backend!"}

# CORS configuration
origins = os.getenv("CORS_ORIGINS", "*").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with proper prefixes
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(project.router, prefix="/projects", tags=["Projects"])
app.include_router(role.router, prefix="/roles", tags=["Roles"])
app.include_router(site_location.router, prefix="/site-location", tags=["Site Location"])
app.include_router(survey_visit.router, prefix="/survey-visit", tags=["Survey Visit"])
app.include_router(site_information.router, prefix="/site-information", tags=["Site Information"])
app.include_router(site_access.router, prefix="/site-access", tags=["Site Access"])
app.include_router(site_session.router)
