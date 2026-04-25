from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float

books = []

@app.get("/")
def home():
    return {"message": "Library Book System API"}

@app.post("/books")
def add_book(book: Book):
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    books.append(book)
    return {"message": "Book added successfully", "book": book}

@app.get("/books")
def get_books(skip: int = 0, limit: int = 10):
    return books[skip: skip + limit]

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}")
def update_book(book_id: int, updated: Book):
    for i, book in enumerate(books):
        if book.id == book_id:
            books[i] = updated
            return {"message": "Book updated"}
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            books.pop(i)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/search")
def search_books(title: Optional[str] = None, author: Optional[str] = None):
    result = books
    if title:
        result = [b for b in result if title.lower() in b.title.lower()]
    if author:
        result = [b for b in result if author.lower() in b.author.lower()]
    return result

@app.get("/sort")
def sort_books(order: str = Query("asc")):
    return sorted(books, key=lambda x: x.price, reverse=(order == "desc"))
