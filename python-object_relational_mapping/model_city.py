#!/usr/bin/python3
"""
 python file that contains the class definition
 of a Cities and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
import sys


class City(Base):
    """
    State class that links to the MySQL table 'cities'
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),  nullable=False)
