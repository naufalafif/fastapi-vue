from app.src.database import Session
from contextlib import contextmanager
import sqlalchemy

@contextmanager
def session_manager():
    """
    sqlalchemy session with context applied to make sure session closed

    :param:
    :return:

    Example:
        >>> from app.src.database.models.books import Book
        >>> with session_manager() as db:
        >>>     result = db.query(Book).all()
    """

    session = Session()
    try:
        yield session
    except Exception as error:
        print("rollback transaction")
        session.rollback()
        raise error
    finally:
        print("closing session connection")
        session.close()