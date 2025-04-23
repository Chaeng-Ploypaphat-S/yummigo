from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    register_date = Column(String, nullable=False)
    type = Column(String, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type,         
    }
    
class Food(Base):
    __tablename__ = 'food'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    
    # Back reference to Foodie
    foodies = relationship(
        'Foodie',
        secondary='foodie_food',
        back_populates='favorite_foods'
    )
    
class Foodie_Food(Base):
    __tablename__ = 'foodie_food'

    id = Column(Integer, primary_key=True)
    foodie_id = Column(Integer, nullable=False)
    food_id = Column(Integer, ForeignKey('food.id'), nullable=False)

class Foodie(User):
    __tablename__ = 'foodie'

    id = Column(Integer, primary_key=True)
    phone = Column(String, unique=True, index=True, nullable=True)

    # Relationship to access favorite foods
    favorite_foods = relationship(
        'Food',
        secondary='foodie_food',
        back_populates='foodies'
    )
    
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
    
