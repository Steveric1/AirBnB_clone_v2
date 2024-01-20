#!/usr/bin/python3

from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """
    private class attribute:
       __engine: sqlalchemy engine
       __session: sqlalchemy session
    
    """
    
    __engine = None
    __session = None
    
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """This  method must return a dictionary"""
        if cls is None:
            obj = self.__session.query(Amenity).all()
            obj.extend(self.__session.query(City).all())
            obj.extend(self.__session.query(Place).all())
            obj.extend(self.__session.query(Review).all())
            obj.extend(self.__session.query(State).all())
            obj.extend(self.__session.query(User).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
                obj = self.__session.query(cls)
        
        return {"{}.{}".format(type(obj).__name__, obj.id): val for val in obj}
    
    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)
    
    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    
    def close(self):
        """"Close working sqlalchemy session"""
        self.__session.close()