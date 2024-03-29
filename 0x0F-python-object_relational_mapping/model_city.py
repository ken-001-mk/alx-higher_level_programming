#!/usr/bin/python3
"""script that Inherits from SQLAlchemy Base and links to the MySQL table cities
"""

from sqlalchemy.ext.declarative import declaractive_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class City(Base):
    """Represents a city for a MySQL database
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
