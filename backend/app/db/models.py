from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    tag = Column(String, unique=True, index=True, nullable=True)
    register_date = Column(String, nullable=False)
    end_date = Column(String, nullable=True)
    password = Column(String, nullable=False)
    type = Column(String, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type,         
    }

class Foodie(User):
    __tablename__ = 'foodie'

    id = Column(Integer, primary_key=True)
    phone = Column(String, unique=True, index=True, nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'foodie',
    }

class Eatery(User):
    __tablename__ = 'eatery'

    id = Column(Integer, primary_key=True)
    website = Column(String, unique=True, index=True, nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'eatery', 
    }