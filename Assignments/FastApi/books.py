from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional

books_db = {
    'Python Data Science Handbook': {'book_name':'Python Data Science Handbook', 'author':'Jake VanderPlas', 'published':2016, 'price':50},
    'Data Science from Scratch': {'book_name':'Data Science from Scratch', 'author':'Joel Grus', 'published':2019, 'price':28},
    'Storytelling with Data': {'book_name':'Storytelling with Data', 'author':'Cole Nussbaumer Knaflic', 'published':2015, 'price':22},
}

class Book(BaseModel):
    book_name: str = Field(min_length=5, max_length=50)
    author: str = Field(None, min_length=5, max_length=50)
    published: Optional[int] = None
    price: int = Field(gt=10, lt=99) # ge: greater than or equal, le: less than or eqaul

class BookUpdate(Book):
    book_name:  str = Field(min_length=5, max_length=50)
    price: int = Field(gt=5, lt=500)

def validateBookName(book_name: str):
    if book_name not in books_db:
        raise HTTPException(status_code=404, detail=f'Book name "{book_name}" was not found.')

app = FastAPI()

@app.get('/books')
def get_books():
    books_list = list(books_db.values())
    return books_list

@app.get('/book/{bookname}')
def get_book(bookname):
    validateBookName(bookname)
    return books_db[bookname]

@app.post('/book')
def add_book(book: Book):
    book_name = book.book_name
    if book_name in books_db:
        raise HTTPException(status_code=409, detail=f'Cannot add book. Book {book_name} already exists')
    books_db[book_name] = book.model_dump()
    return {'message': f'Successfully added the book: {book_name}'}

@app.delete('/book/{bookname}')
def delete_book(bookname):
    validateBookName(bookname)
    del books_db[bookname]
    return {'message': f'Successfully deleted the book: {bookname}'}

@app.put('/book')
def update_book(book: Book):
    book_name = book.book_name
    validateBookName(book_name)
    books_db[book_name] = book.model_dump()
    return {'message': f'Successfully updated the book: {book_name}'}

@app.patch('/book')
def update_book_partial(book: BookUpdate):
    book_name = book.book_name
    validateBookName(book_name)
    books_db[book_name].update(book.model_dump(exclude_unset=True))
    return {'message': f'Successfully updated the book: {book_name}'}
