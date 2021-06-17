import pandas as pd
from sqlalchemy.sql.functions import session_user
from base import Base, Engine, Session
from cards import Cards
from extra_data import TypesData, StatsData


def run():
    Base.metadata.create_all(Engine)
    session = Session()
    cards = pd.read_csv('clean_cards.csv')
    types_data = pd.read_csv('clean_types.csv')
    stats_data = pd.read_csv('clean_stats.csv')
    
    
    for index, row in cards.iterrows():
        card = Cards(row['uid'], row['name'], row['type'], row['stats'],
                     row['colection'], row['description'], row['card_link'])
        session.add(card)
        
    for index, row in types_data.iterrows():
        typess = TypesData(row['types'], row['count'], row['percentage'])
        session.add(typess)
        
    for index, row in stats_data.iterrows():
        stat = StatsData(row['stats'], row['count'], row['percentage'])
        session.add(stat)
        
    
    session.commit()
    session.close()


if __name__ == '__main__':
    run()