"""
Simple FastAPI REST API server for managing authors.
Data is stored in-memory using a dictionary (no database).

Example POST request JSON:
{
    "id": 7,
    "name": "George Orwell",
    "birth_year": 1903,
    "country_of_birth": "India",
    "first_published_date": "1933",
    "death_date": "1950"
}
"""

from datetime import datetime
from typing import Optional, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


# Author model
class Author(BaseModel):
    id: int = Field(..., description="Unique identifier for the author")
    name: str = Field(..., description="Full name of the author")
    birth_year: int = Field(..., description="Year the author was born")
    country_of_birth: str = Field(..., description="Country where the author was born")
    first_published_date: str = Field(..., description="Date of first published book")
    death_date: Optional[str] = Field(None, description="Death date (if applicable)")


# In-memory storage
authors_db: Dict[int, Author] = {}


# Initialize FastAPI app
app = FastAPI(
    title="Authors REST API",
    description="A simple REST API for managing author information",
    version="1.0.0"
)


@app.on_event("startup")
async def load_initial_data():
    """Load initial authors into the in-memory database at startup."""
    initial_authors = [
        Author(
            id=1,
            name="J.R.R. Tolkien",
            birth_year=1892,
            country_of_birth="South Africa",
            first_published_date="1937",
            death_date="1973"
        ),
        Author(
            id=2,
            name="Ernest Hemingway",
            birth_year=1899,
            country_of_birth="United States",
            first_published_date="1926",
            death_date="1961"
        ),
        Author(
            id=3,
            name="F. Scott Fitzgerald",
            birth_year=1896,
            country_of_birth="United States",
            first_published_date="1920",
            death_date="1940"
        ),
        Author(
            id=4,
            name="Willa Cather",
            birth_year=1873,
            country_of_birth="United States",
            first_published_date="1903",
            death_date="1947"
        ),
        Author(
            id=5,
            name="Joan Didion",
            birth_year=1934,
            country_of_birth="United States",
            first_published_date="1963",
            death_date="2021"
        ),
        Author(
            id=6,
            name="Thomas Wolfe",
            birth_year=1900,
            country_of_birth="United States",
            first_published_date="1929",
            death_date="1938"
        ),
    ]
    
    for author in initial_authors:
        authors_db[author.id] = author


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Authors REST API",
        "endpoints": {
            "GET /authors": "Get all authors",
            "GET /author/{id}": "Get author by ID",
            "POST /author": "Create a new author"
        }
    }


@app.get("/authors")
async def get_authors():
    """Get all authors."""
    return {"authors": list(authors_db.values())}


@app.get("/author/{author_id}")
async def get_author(author_id: int):
    """Get a specific author by ID."""
    if author_id not in authors_db:
        raise HTTPException(status_code=404, detail=f"Author with id {author_id} not found")
    return authors_db[author_id]


@app.post("/author", status_code=201)
async def create_author(author: Author):
    """Create a new author."""
    if author.id in authors_db:
        raise HTTPException(status_code=400, detail=f"Author with id {author.id} already exists")
    
    authors_db[author.id] = author
    return {"message": "Author created successfully", "author": author}
