from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundoclient(client):
    response = client.get('/')  # Act (Ação)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá mundo!'}


def teste_create_user(client):
    response = client.post(  # UserSchema
        '/users/',
        json={
            'username': 'testeusername',
            'password': 'password',
            'email': 'teste@teste.com',
        },
    )

    # Voltou o staus code correto?
    assert response.status_code == HTTPStatus.CREATED
    # Validar UserPublic
    assert response.json() == {
        'username': 'testeusername',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        'users': [
            {
                'username': 'testeusername',
                'email': 'teste@teste.com',
                'id': 1,
            }
        ]
    }
