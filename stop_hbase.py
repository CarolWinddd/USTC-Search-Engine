import subprocess
import os

hadoop_dir = 'E:\\HBase\\hadoop\\sbin'
command_hadoop = 'stop-all.cmd'

hbase_dir = 'E:\\HBase\\hbase\\bin'
command_hbase = 'stop-hbase.cmd'

command_thrift = 'hbase thrift stop'

subprocess.run(command_hadoop,cwd=hadoop_dir,shell=True)
print('Hadoop stoped successfully!')
subprocess.run(command_hbase,cwd=hbase_dir,shell=True)
print('HBase stoped successfully!')
subprocess.run(command_thrift,cwd=hbase_dir,shell=True)
print('All stoped successfully!')