import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)
    password = Column(String(32))

class Planets(Base):
       __tablename__ = 'planets'
       id = Column(Integer, primary_key=True)
       name = Column(String(50))
       population = Column(Integer)

class FavoritePlanets(Base):
      __tablename__ = 'favoriteplanets'
      id = Column(Integer, primary_key=True)
      user_id = Column(Integer, ForeignKey('user.id'))
      user_id_relationship = relationship(User)
      planets_id = Column(Integer, ForeignKey('planets.id'))
      planets_id_relationship = relationship(Planets)

class Characters(Base):
      __tablename__ = 'characters'
      id = Column(Integer, primary_key=True)
      name = Column(String(50))
      height = Column(Integer)
      mass = Column(Integer)
      gender = Column(String(50))

class FavoriteCharacters(Base):
      __tablename__ = 'favoritecharacters'
      id = Column(Integer, primary_key=True)
      user_id = Column(Integer, ForeignKey('user.id'))
      user_id_relationship = relationship(User)
      characters_id = Column(Integer, ForeignKey('characters.id'))
      characters_id_relationship = relationship(Characters)
      
class Starships(Base):
      __tablename__ = 'starships'
      id = Column(Integer, primary_key=True)
      name = Column(String(50))
      model = Column(String(50))
      manufacturer = Column(String(50))
      cost_in_credits = Column(Integer)

class FavoriteStarships(Base):
      __tablename__ = 'favoritestarships'
      id = Column(Integer, primary_key=True)
      user_id = Column(Integer, ForeignKey('user.id'))
      user_id_relationship = relationship(User)
      starships_id = Column(Integer, ForeignKey('starships.id'))
      starships_id_relationship = relationship(Starships)
      
      

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
