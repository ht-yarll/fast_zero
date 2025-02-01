from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='yarll', email='yar@ll.com', password='password')
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 'yar@ll.com'))

    assert result.username == 'yarll'
