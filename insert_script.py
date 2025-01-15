import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://admin:admin@postgres:5432/demo_db")

df = pd.read_csv('https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2020-05.csv.gz', low_memory=False)

df.to_sql(con=engine, name='yellow_demo', if_exists='replace')