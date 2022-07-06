from pyhive import hive
import pandas as pd

#Create Hive connection
conn = hive.Connection(host="192.186.177.128", port=10000, username="hive")

# Read Hive table and Create pandas dataframe
df = pd.read_sql("SELECT * FROM default.pizza2", conn)
print(df.head())