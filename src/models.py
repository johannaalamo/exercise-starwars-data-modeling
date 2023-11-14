import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    nombre = Column(String(250))
    apellido = Column(String(250))

    favoritos = relationship('Favorito', back_populates='usuario')

class Planeta(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)

    favoritos = relationship('Favorito', back_populates='planeta')

class Personaje(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)

    favoritos = relationship('Favorito', back_populates='personaje')

class Favorito(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    planeta_id = Column(Integer, ForeignKey('planetas.id'))
    personaje_id = Column(Integer, ForeignKey('personajes.id'))

    usuario = relationship('Usuario', back_populates='favoritos')
    planeta = relationship('Planeta', back_populates='favoritos')
    personaje = relationship('Personaje', back_populates='favoritos')


render_er(Base, 'diagram.png')