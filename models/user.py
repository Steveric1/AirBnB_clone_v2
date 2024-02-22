# #!/usr/bin/python3
# """This module defines a class User"""
# from models.base_model import BaseModel, Base
# from sqlalchemy import Column, String
# from sqlalchemy.orm import relationship
# 
# 
# class User(BaseModel, Base):
#     """This class defines a user by various attributes"""
#     __tablename__ = 'users'
# 
#     email = Column(String(128), nullable=False)
#     password = Column(String(128), nullable=False)
#     first_name = Column(String(128))
#     last_name = Column(String(128))
# 


from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User

    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name
        last_name (str): last name

    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""