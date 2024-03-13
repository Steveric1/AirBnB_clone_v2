#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel
from models.city import City
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")
    
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ returns the list of City instances with state_id
            equals to the current State.id"""
            
            list_city = []
            
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    list_city.append(city)
            
            return list_city
            

# from models.base_model import BaseModel
# 
# 
# class State(BaseModel):
#     """State class that inherits from BaseModel."""
#     name: str = ""