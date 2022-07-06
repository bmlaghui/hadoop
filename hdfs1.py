import pandas as pd
from hdfs import InsecureClient

client = InsecureClient('http://192.168.177.128:9000', user='cloudera')

from json import dump, dumps
records = [
  {'name': 'foo', 'weight': 1},
  {'name': 'bar', 'weight': 2},
]

# As a context manager:
with client.write('data/records.jsonl', encoding='utf-8') as writer:
  dump(records, writer)

# Or, passing in a generator directly:
client.write('data/records.jsonl', data=dumps(records), encoding='utf-8')


df=pd.read.csv("file.csv")
# with client_hdfs.write('path/output.csv', encoding = 'utf-8') as writer:
#   df.to_csv(writer)