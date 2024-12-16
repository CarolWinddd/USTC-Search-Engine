import subprocess
import os

hadoop_dir = 'E:\\HBase\\hadoop\\sbin'
command_hadoop = 'start-all.cmd'

hbase_dir = 'E:\\HBase\\hbase\\bin'
command_hbase = 'start-hbase.cmd'

command_thrift = 'hbase thrift start'

subprocess.run(command_hadoop,cwd=hadoop_dir,shell=True)
print('Hadoop started successfully!')
subprocess.run(command_hbase,cwd=hbase_dir,shell=True)
print('HBase started successfully!')
subprocess.run(command_thrift,cwd=hbase_dir,shell=True)
print('All started successfully!')