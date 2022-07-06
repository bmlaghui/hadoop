import os

import pandas as pd

from subprocess import PIPE, Popen


import pandas as pd
from sqlalchemy import create_engine

SECRET = {'username':'hive', 'password': 'cloudera'}
user_name = SECRET.get('username')
passwd = SECRET.get('password')

host_server = '192.168.177.128'
port = '10000'
database = 'default'
conn = f'hive://{user_name}@{host_server}:{port}/{database}'
engine = create_engine(conn, connect_args={'auth': 'NOSASL'})

# define path to saved file
file_name = "saved_file.csv"

# create a pandas.DataFrame
sales = {'account': ['Jones LLC', 'Alpha Co', 'Blue Inc'], 'Jan': [150, 200, 50]}
df = pd.DataFrame.from_dict(sales)

# save your pandas.DataFrame to csv (this could be anything, not necessarily a pandas.DataFrame)
df.to_csv(file_name)

# create path to your username on hdfs
hdfs_path = os.path.join(os.sep, 'user', '<your-user-name>', file_name)

# put csv into hdfs
put = Popen(["hadoop", "fs", "-put", file_name, hdfs_path], stdin=PIPE, bufsize=-1)
put.communicate()
