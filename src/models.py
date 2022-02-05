import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email= Column (String(50),nullable=False, unique=True)
    password= Column(String(20),nullable=False)

class Planet(Base):
    __tablename__='planet'
    id=Column(Integer,primary_key=True)
    name=Column(String(250),nullable=False, unique=True)
    diameter= Column(Integer)
    rotation_period= Column(Integer)
    orbital_period= Column(Integer)
    gravity=Column(String(20))
    population=Column(Integer)
    climate=Column(String(20))
    terrain=Column(String(50))
    surface_water=Column(Integer)
    created=Column(String(250))
    edited=Column(String(250))
    url=Column(String(250))

class Character(Base):
    __tablename__='character'
    id=Column(Integer,primary_key=True)
    name=Column(String(250),nullable=False, unique=True)
    height=Column(Integer)
    mass=Column(Integer)
    hair_color=Column(String(20))
    skin_color=Column(String(20))
    eye_color=Column(String(20))
    birth_year=Column(String(20))
    gender=Column(String(20))
    created=Column(String(50))
    edited=Column(String(50))
    homeworld=Column(String(250))
    url=Column(String(250))
    planet_id=Column(Integer, ForeignKey('planet.id'))
    planet=relationship(Planet)

class Favorite(Base):
    __tablename__='favorite'
    id=Column(Integer,primary_key=True)
    planet_id=Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id=Column(Integer,ForeignKey('character.id'), nullable=True)
    user_id=Column(Integer,ForeignKey('user.id'))
    planet=relationship(Planet)
    character=relationship(Character)
    user=relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')