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

content_list = [
    {'key': 'content 1', 'name': 'spidyweb 1', 'category': 'web'},
    {'key': 'content 2', 'name': 'test', 'category': 'data'},
    {'key': 'content 3', 'name': 'spidyweb 3', 'category': 'development'},
    {'key': 'content 4', 'name': 'spidyweb 4', 'category': 'governance 4'},
]

# query parameters
# Query parameter는 url에서 특정한 조건을 주고싶을 때 사용하는 매개변수 유형입니다. 같은 API를 호출한다고 해도, 서로 다른 조건으로 나열하는 것이 필요한 상황에 사용
# 127.0.0.1/content/content 1 처럼 입력하면 key가 content 1인 데이터를 get함
@app.get("/content/{content_title}/")
async def read_content(content_title: str):
    for content in content_list:
        if content.get('key').casefold() == content_title.casefold():
            return content

# 127.0.0.1/content/?category=value 처럼 입력하면 관련된 content_list data가 get됨
@app.get("/content/")
async def read_category_by(category: str):
    contents_to_return = []
    for content in content_list:
        if content.get('category').casefold() == category.casefold():
            contents_to_return.append(content)
    return contents_to_return


# path + query parameter 사용 법
@app.get("/content2/{content_name}/")
async def read_name_category_by_query(content_name: str, category: str):
    contents_to_return= []
    for content in content_list:
        if content.get('name').casefold() == content_name.casefold() and \
                content.get('category').casefold() == category.casefold():
            contents_to_return.append(content)
    return contents_to_return


# POST

# PUT

# DELETE
