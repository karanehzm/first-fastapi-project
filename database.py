# connection to the database, this is a database setup and configuration


from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine) 


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


        



