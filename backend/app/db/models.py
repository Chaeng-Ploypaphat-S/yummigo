from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the Base class
Base = declarative_base()

class Foodie(Base):
    __tablename__ = 'foodie'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, unique=True, index=True, nullable=True)
    tag = Column(String, unique=True, index=True, nullable=True)
    register_date = Column(String, nullable=False)
    end_date = Column(String, nullable=True)
    password = Column(String, nullable=False)
    
class Eatery(Base):
    __tablename__ = 'eatery'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    tag = Column(String, unique=True, index=True, nullable=True)
    register_date = Column(String, nullable=False)
    end_date = Column(String, nullable=True)
    password = Column(String, nullable=False)