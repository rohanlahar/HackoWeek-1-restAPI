from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Library Management API")

# 1. Data validation schema
class BookInput(BaseModel):
    title: str
    author: str
    available: Optional[bool] = True

# 2. In-memory data store acting as our task database
database = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "available": True},
    {"id": 2, "title": "1984", "author": "George Orwell", "available": False}
]

# 3. GET: Retrieve all books
@app.get("/api/books")
def get_all_books():
    return database

# 4. POST: Add a new book
@app.post("/api/books")
def add_book(book: BookInput):
    new_book = {
        "id": len(database) + 1,
        "title": book.title,
        "author": book.author,
        "available": book.available
    }
    database.append(new_book)
    return new_book

# 5. PUT: Update a book's details or availability status
@app.put("/api/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    for item in database:
        if item["id"] == book_id:
            item["title"] = book.title
            item["author"] = book.author
            item["available"] = book.available
            return {"message": f"Book {book_id} updated successfully", "book": item}
    raise HTTPException(status_code=404, detail="Book not found")

# 6. DELETE: Remove a book from the library by its ID
@app.delete("/api/books/{book_id}")
def delete_book(book_id: int):
    for index, item in enumerate(database):
        if item["id"] == book_id:
            database.pop(index)
            return {"message": f"Book {book_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
