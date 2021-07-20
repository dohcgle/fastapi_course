from fastapi import FastAPI, Query, Path, Body
from schemas import Book, BookOut

app = FastAPI()

@app.post('/book', response_model=BookOut, response_model_exclude_unset=True)
def create_book(item: Book):
    return BookOut(**item.dict(), id=3)


# @app.post('/book')
# def create_book(item: Book, author:Author, quantity: int = Body(...)):
#     return {"item": item, "author": author, "quantity": quantity}
#
# @app.post('/author')
# def create_author(author:Author = Body(..., embed=True)):
#     return {"author": author}
#
# @app.get('/book')
# def get_book(q: str = Query(..., min_length=2, max_length=5, description='Search book')):
#     return q
#
# @app.get('/book/{pk}')
# def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):
#     return {"pk": pk, "pages": pages}