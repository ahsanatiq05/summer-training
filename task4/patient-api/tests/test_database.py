from app.database import create_db_and_tables, get_session

def test_create_db_and_tables():
    create_db_and_tables()


def test_get_session():
    gen = get_session()
    session = next(gen)
    assert session is not None
    gen.close()