from pyhive import hive
import pandas as pd
import sqlalchemy
from sqlalchemy.engine import create_engine
import datetime
from subprocess import PIPE, Popen
import subprocess
import sys

conn = hive.Connection(host="192.168.177.128", port=10000, username="hive")
cursor = conn.cursor()

query="select user_id,country from test_dev_db.test_data"

start_time= datetime.datetime.now()

output_file='./restaurants-casvp.json'

data=pd.read_sql(query,conn)
data['current_date'] = pd.datetime.today().strftime("%Y-%m-%d")
print(data)

data.to_csv(output_file, sep='|', encoding='utf-8',index=None)

hivequery=""" hive --hivevar loaded_date=$(date +"%Y-%m-%d") hive -e 'LOAD DATA LOCAL INPATH "/home/vikct001/user/vikrant/python/test_data.csv" INTO TABLE test_dev_db.test_data_external PARTITION (loaded_date="${hivevar:loaded_date}")';"""

def save_to_hdfs(output_file):
        print("I am here")
        p=subprocess.Popen(hivequery,shell=True,stderr=subprocess.PIPE)
        stdout,stderr = p.communicate()
        if p.returncode != 0:
            print (stderr)
            sys.exit(1)


save_to_hdfs(output_file)
end_time=datetime.datetime.now()

print ('processing ends', (start_time-end_time).seconds/60.0,' minutes')
