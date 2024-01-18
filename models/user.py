#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine('mysql://root:password@locahost/hbnb_dev_db', echo=True)
# Base = declarative_base()

class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'user'
    
    # id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

# Base.metadata.create_all(engine)
