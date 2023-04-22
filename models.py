from datetime import datetime

from sqlalchemy import create_engine, Column, DateTime, Integer, String, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session


LINES_COUNT = 6


def create_schema_and_fill():
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    for _ in range(LINES_COUNT):
        session.add(CookieProfile())

    session.commit()

    return session


Base = declarative_base()
engine = create_engine('sqlite:///profile.db', connect_args={'timeout': 15})


class CookieProfile(Base):

    __tablename__ = 'cookie_profile'

    id = Column(Integer(), primary_key=True)
    created_on = Column(DateTime(), default=datetime.now())
    cookies_value = Column(BLOB())
    last_start_on = Column(DateTime())
    number_of_starts = Column(Integer(), default=0)
