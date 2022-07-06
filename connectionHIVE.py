import json

import pandas as pd
from sqlalchemy import create_engine

SECRET = {'username':'hive', 'password': 'cloudera'}
user_name = SECRET.get('username')
passwd = SECRET.get('password')

host_server = '192.168.177.128'
port = '10000'
database = 'Restaurants'
conn = f'hive://{user_name}@{host_server}:{port}/{database}'
engine = create_engine(conn, connect_args={'auth': 'NOSASL'})

query = "select * from restaurants"
data = pd.read_sql(query, con=engine)
print(data)
