from fastapi import FastAPI


# app 변수에 FastAPI 인스턴스 생성
app = FastAPI()

book = [{"key":"value"}]

# 비동기로 def하는 이유는?
# / 경로에 아래와 같은 api를 호출, endpoint지정과 같음
@app.get("/")
async def first_api():
    return {"message": "Hello spidyweb!"}

@app.get("/api-endpoint")
async def read_api_endpoint():
    return book

# swagger 127.0.0.1:8000/docs

# 동적 api를 사용할 때는 정적 API를 항상 앞에 둬야 함(python interpreter 특징)
@app.get("/books/mybook")
async def read_all_books():
    return {'book_title': 'My book!'}

@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param: str):
    return {'dynamic_param': dynamic_param}

# endpoint에 띄어쓰기를 사용할 때는 아래와 같이 하지만, 실제 url은 다음과 같이 나옴 http://127.0.0.1:8000/space/my%20book
@app.get("/space/my book")
async def space_test():
    return {'space': 'space!'}