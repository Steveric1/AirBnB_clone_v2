# #!/usr/bin/python3
# """ Review module for the HBNB project """
# from models.base_model import BaseModel
# 
# 
# class Review(BaseModel):
#     """ Review classto store review information """
#     place_id = ""
#     user_id = ""
#     text = ""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    A subclass of BaseModel class
    Public class attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    place_id: str = ""
    user_id: str = ""
    text: str = ""