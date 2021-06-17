from sqlalchemy import Column, String, Integer, Float
from base import Base


class TypesData(Base):
    __tablename__ = 'types_extra_data'
    typess = Column(String, primary_key=True)
    count = Column(Integer)
    percentages = Column(Float)
    
    def __init__(self, typess, count, percentages):
        self.typess = typess
        self.count = count
        self.percentages = percentages
        
class StatsData(Base):
    __tablename__ = 'stats_extra_data'
    stats = Column(String, primary_key=True)
    count = Column(Integer)
    percentages = Column(Float)
    
    def __init__(self, stats, count, percentages):
        self.stats = stats
        self.count = count
        self.percentages = percentages