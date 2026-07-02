from fastapi import FastAPI

app = FastAPI()

books = []

@app.get("/books")
def ge_all_books():
    return {
        "books": books,
        "total": len(books)
    }

@app.post("/books")
def add_book(book: dict):
    books.append(book)
    return {
        "message": "Book added successfully!",
        "books": books,
        "total_books": len(books)
    }