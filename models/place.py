# #!/usr/bin/python3
# """ Place Module for HBNB project """
# from models.base_model import BaseModel
# # from sqlalchemy import Column, String, Integer, ForeignKey
# 
# 
# class Place(BaseModel):
#     """ A place to stay """
#     city_id = ""
#     user_id = ""
#     name = ""
#     description = ""
#     number_rooms = 0
#     number_bathrooms = 0
#     max_guest = 0
#     price_by_night = 0
#     latitude = 0.0
#     longitude = 0.0
#     amenity_ids = []
#     
#     # __tablename__ = 

from models.base_model import BaseModel
from typing import List


class Place(BaseModel):
    """
    A subclass of BaseModel class
    Public class attributes:
        city_id: string - empty string: it will be the City.id
        user_id: string - empty string: it will be the User.id
        name:     (str)
        description: string - empty string
        number_rooms: integer - 0
        number_bathrooms: integer - 0
        max_guest: integer - 0
        price_by_night: integer - 0
        latitude: float - 0.0
        longitude: float - 0.0
        amenity_ids: list of string - empty list: it will be
        the list of Amenity.id later
    """
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: List[str] = []