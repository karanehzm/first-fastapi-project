# what our database contains, structure of the database

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()   #a base calss that out database models will inherit from

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    age = Column(Integer)

    workspaces = relationship("Workspace", back_populates = "owner")


class Workspace(Base):
    __tablename__ = "workspaces"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete= "CASCADE"), nullable = False)

    owner = relationship("User", back_populates = "workspaces")


