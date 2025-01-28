from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserID, UserPublic, UserSchema

app = FastAPI()
database = []


@app.get('/', response_model=Message)
def read_root():
    return {'message': 'Hellou World🌎'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserID(id=len(database) + 1, **user.model_dump())

    database.append(user_with_id)

    return user_with_id
