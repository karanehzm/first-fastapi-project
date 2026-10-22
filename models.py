# what our database contains, structure of the database

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint

Base = declarative_base()   #a base calss that out database models will inherit from

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    age = Column(Integer)

    workspaces = relationship("Workspace", back_populates = "owner")
    memberships = relationship("WorkspaceMember", back_populates = "user")

   

class Workspace(Base):
    __tablename__ = "workspaces"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete= "CASCADE"), nullable = False)

    owner = relationship("User", back_populates= "workspaces")
    memberships = relationship("WorkspaceMember", back_populates= "workspace")

   


class WorkspaceMember(Base):
    __tablename__ = "workspace_member"
    __table_args__ = (
    UniqueConstraint(
        "user_id",
        "workspace_id",
        name="uq_workspace_member_user_workspace"
    ),
    )

    id = Column(Integer, primary_key = True)
    user_id = Column(
        Integer, 
        ForeignKey("users.id", onupdate="CASCADE") ,
        nullable = False )
    
    workspace_id = Column(
        Integer,
        ForeignKey("workspaces.id", ondelete = "CASCADE"),
        nullable = False)

   
    user = relationship("User", back_populates= "memberships")
    workspace = relationship("Workspace", back_populates= "memberships")


