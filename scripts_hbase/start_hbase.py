import subprocess
import json

with open('scripts_hbase/config_hbase.json', 'r') as f:
    config = json.load(f)

hadoop_dir = config['hadoop_dir']
command_hadoop = 'start-all.cmd'

hbase_dir = config['hbase_dir']
command_hbase = 'start-hbase.cmd'

command_thrift = 'hbase thrift start'

subprocess.run(command_hadoop,cwd=hadoop_dir,shell=True)
print('Hadoop started successfully!')
subprocess.run(command_hbase,cwd=hbase_dir,shell=True)
print('HBase started successfully!')
subprocess.run(command_thrift,cwd=hbase_dir,shell=True)
print('All started successfully!')