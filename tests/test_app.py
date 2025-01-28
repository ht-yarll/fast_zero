from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_should_return_ok_e_hellouworld():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hellou World🌎'}


def test_create_user():
    client = TestClient(app)

    response_post = client.post(
        '/users/',
        json={
            'username': 'test_username',
            'email': 'test@test.com',
            'password': 'password',
        },
    )
    assert response_post.status_code == HTTPStatus.CREATED
    assert response_post.json() == {
        'id': 1,
        'username': 'test_username',
        'email': 'test@test.com',
    }
