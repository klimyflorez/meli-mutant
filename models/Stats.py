from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, Boolean

Base = declarative_base()
class Stast(Base):
    __tablename__ = 'stats'

    id = Column('id', Integer(), primary_key=True, autoincrement=True)
    entity_id = Column(Text())
    is_mutant = Column(Boolean())

    def __init__(self,entity_id,is_mutant):
        self.entity_id = entity_id
        self.is_mutant = is_mutant