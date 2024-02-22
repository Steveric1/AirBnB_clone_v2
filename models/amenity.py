# #!/usr/bin/python3
# """ State Module for HBNB project """
# from models.base_model import BaseModel
# 
# 
# class Amenity(BaseModel):
#     name = ""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A subclass of BaseModel class
    Public class attributes:
        name:     (str)
    """
    name: str = ""