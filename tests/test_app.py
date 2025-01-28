from http import HTTPStatus


def test_read_root_should_return_ok_e_hellouworld(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hellou World🌎'}


def test_create_user(client):
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


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'test_username',
                'email': 'test@test.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'test_username_updated',
            'email': 'test_updated@test.com',
            'password': 'password_updated',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'test_username_updated',
        'email': 'test_updated@test.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
