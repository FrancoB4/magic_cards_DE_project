from sqlalchemy import Column, String
from base import Base


class Cards(Base):
    __tablename__ = 'Cards'
    ids = Column(String, primary_key=True)
    names = Column(String)
    types = Column(String)
    stats = Column(String)
    collections = Column(String)
    descriptions = Column(String)
    urls = Column(String)

    def __init__(self, uids, names, types, stats,
                 collections, descriptions, urls):
        self.ids = uids
        self.names = names
        self.types = types
        self.stats = stats
        self.collections = collections
        self.descriptions = descriptions
        self.urls = urls
