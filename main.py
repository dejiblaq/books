#creating a book resource
#retrieve a book resource
#update a book resource
#delete a book resource
from fastapi import FastAPI, Response

app = FastAPI()

# Sample data for books
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1", "year": 2020},
    {"id": 2, "title": "Book 2", "author": "Author 2", "year": 2021},
    {"id": 3, "title": "Book 3", "author": "Author 3", "year": 2022},
]

# Retrieve all books
@app.get("/books/")
def get_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}

@app.get("/books/{books}")
def get_book_author(author: str = None):
    if author is None:
        return books
    for book in books:
        if book["author"] == author:
            return book
    return {"error": "Book not found"}

   
    ''' author_books = [book for book in books if book["author"] == author]
if author_books:
    return author_books
return {"error": "No books found for the given author"}'''

@app.post("/books/")
def create_book(title: str, author: str, year: int):
    new_book = {
        "id": len(books) + 1, 
        "title": title, 
        "author": author, 
        "year": year
    }
    books.append(new_book)
    return new_book

@app.put("/books/{book_id}")
def update_book(book_id: int, title: str, author: str, year: int):
    for book in books:
        if book["id"] == book_id:
            book["title"] = title
            book["author"] = author
            book["year"] = year
            return book
    return {"error": "Book not found"}


@app.patch("/books/{book_id}")
def update_book(book_id: int, title: str = None, author: str = None, year: int = None):
    for book in books:
        if book["id"] == book_id:
            if title:
                book["title"] = title
            if author:
                book["author"] = author
            if year:
                book["year"] = year
            return book
    return {"error": "Book not found"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    '''for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted"}'''
    
    for index, book in enumerate(books):
        if book["id"] == book_id:
            del books[index]
            return {"message": "Book deleted"}
    return {"error": "Book not found"}

    '''book = next((book for book in books if book["id"] == book_id), None)

    if book is None:
        return {"error": "Book not found"}
    books.remove(book)
    return {"message": "Book deleted"}'''

    '''book = next((book for book in books if book["id"] == book_id), None)
    if book is None:
        return Response(status_code=404, content="Book not found")
    books.remove(book)
    return Response(status_code=204, content="Book deleted")'''

