from dataclasses import asdict

from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(username='yarll', email='yar@ll.com', password='password')
        session.add(new_user)
        session.commit()
        user = session.scalar(select(User).where(User.username == 'yarll'))

    assert asdict(user) == {
        'id': 1,
        'username': 'yarll',
        'password': 'password',
        'email': 'yar@ll.com',
        'created_at': time,
        'updated_at': time
    }
