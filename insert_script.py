import pandas as pd
from sqlalchemy import create_engine

print('Creating Engine')
engine = create_engine("postgresql+psycopg2://admin:admin@postgres:5432/demo_db")

print('Reading CSV')
df = pd.read_csv('https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv', low_memory=False)

print('Inserting Records')

try:
    df.to_sql(con=engine, name='taxi_zones', if_exists='append')
except Exception as e:
    print(f"Oops encounterd an issue {str(e)}")