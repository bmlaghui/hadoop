import subprocess

proc = subprocess.Popen(['hdfs', 'dfs', '-copyFromLocal', './restaurants-casvp.csv', '192.18.177.128:9000/des'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
s_output, s_err = proc.communicate()
s_return =  proc.returncode
