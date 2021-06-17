from os import name
import pandas as pd
import hashlib


def run():
    cards_df = pd.read_csv('../../cards.csv') # cambiar esto
    cards_df.drop_duplicates(subset=['name'], keep='first', inplace=True)

    cards_df = generate_index(cards_df)
    
    types_info = types_data(cards_df)
    stats_info = stats_data(cards_df)
    
    save_file(cards_df, 'cards.csv')
    save_file(types_info, 'types.csv')
    save_file(stats_info, 'stats.csv')
    

def generate_index(df):
    uids = (df
            .apply(lambda row: hashlib.md5(bytes(row['name'].encode())), axis=1)
            .apply(lambda hash_obj: hash_obj.hexdigest())
            )
    df['uid'] = uids
    df.set_index('uid', inplace=True)
    return df


def types_data(df):
    total_cards = len(df.values)
    
    types_count = df['type'].value_counts()
    types_count_percentage = pd.Series([round((row/total_cards)*100, 2) for row in types_count])
    
    types_df = pd.DataFrame()
    types_df['count'] = types_count.values
    types_df['percentage'] = types_count_percentage.values
    types_df['types'] = types_count.index
    types_df.set_index(['types'], inplace=True)
    
    types_df = types_df[types_df['count'] >= 3]
    
    return types_df


def stats_data(df):
    total_cards = len(df.values)
    
    stats_count = df['stats'].value_counts().drop('-')
    stats_count_percentage = pd.Series([round((row/total_cards)*100, 2) for row in stats_count])
    
    stats_df = pd.DataFrame()
    stats_df['count'] = stats_count.values
    stats_df['percentage'] = stats_count_percentage.values
    stats_df['stats'] = stats_count.index
    stats_df.set_index(['stats'], inplace=True)
    
    stats_df = stats_df[stats_df['count'] > 3]
    
    return stats_df


def save_file(df, filename):
    clean_filename = 'clean_' + filename
    df.to_csv(clean_filename, encoding='utf-8')


if __name__ == '__main__':
    run()
