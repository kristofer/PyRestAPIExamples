# PyRestAPIExamples
A simple FastAPI REST API server example. NO Database. Just a dictionary in memory for data.

## Description
This is a simple REST API for managing author information using FastAPI. The data is stored in-memory using a Python dictionary and is loaded at startup with six famous authors.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kristofer/PyRestAPIExamples.git
cd PyRestAPIExamples
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

Start the FastAPI server with:
```bash
uvicorn main:app --reload
```

The server will be available at `http://localhost:8000`

## API Endpoints

### GET /
Root endpoint with API information.

### GET /authors
Get all authors.

**Example:**
```bash
curl http://localhost:8000/authors
```

### GET /author/{id}
Get a specific author by ID.

**Example:**
```bash
curl http://localhost:8000/author/1
```

### POST /author
Create a new author.

**Example:**
```bash
curl -X POST http://localhost:8000/author \
  -H "Content-Type: application/json" \
  -d '{
    "id": 7,
    "name": "George Orwell",
    "birth_year": 1903,
    "country_of_birth": "India",
    "first_published_date": "1933",
    "death_date": "1950"
  }'
```

## Initial Authors

The API is preloaded with the following authors:

1. J.R.R. Tolkien (1892-1973) - South Africa
2. Ernest Hemingway (1899-1961) - United States
3. F. Scott Fitzgerald (1896-1940) - United States
4. Willa Cather (1873-1947) - United States
5. Joan Didion (1934-2021) - United States
6. Thomas Wolfe (1900-1938) - United States

## Author Model

Each author has the following fields:
- `id` (integer): Unique identifier
- `name` (string): Full name
- `birth_year` (integer): Year of birth
- `country_of_birth` (string): Country of birth
- `first_published_date` (string): Date of first published book
- `death_date` (string, optional): Death date if applicable

## Interactive API Documentation

FastAPI automatically generates interactive API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
