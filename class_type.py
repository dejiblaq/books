from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class BookBase(BaseModel):
    title: str
    author: str
    year: int

class Book(BookBase):
    id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookPatch(BaseModel):
    title: Optioanl[str] = None
    author: Optional[str] = None
    year: Optional[int] = None




books = [
    Book(id=1, title="The Catcher in the Rye", author="J.D. Salinger", year=1951),
    Book(id=2, title="To Kill a Mockingbird", author="Harper Lee", year=1960),
    Book(id=3, title="1984", author="George Orwell", year=1949),
]

@app.get("/books/", response_model=list[Book])
async def read_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books/", response_model=Book)
async def create_book(book: BookCreate):
    new_book: Book  = Book(id=len(books) + 1, **book.model_dump())
    books.append(new_book)
    return new_book

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, book: BookUpdate):
    for i, existing_book in enumerate(books):
        if existing_book.id == book_id:
            books[i].title = book.title
            books[i].author = book.author
            books[i].year = book.year
            # books[i] = Book(id=book_id, **book.model_dump())
            return books[i]
    raise HTTPException(status_code=404, detail="Book not found")
           
    

@app.patch("/books/{book_id}", response_model=Book)
async def patch_book(book_id: int, book: BookPatch):
    for i, existing_book in enumerate(books):
        if existing_book.id == book_id:
            updated_book_data = existing_book.model_copy(update=book.model_dump(exclude_unset=True))
            books[i] = updated_book_data
            return books[i]
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            del books[i]
            return {"message": "Book deleted"}


