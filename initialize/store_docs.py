import happybase
import json
import sys
import os

# add the path of the project to sys.path
sys.path.append(os.path.dirname(__file__)+'/..')
from utils.docs import doc_to_bytes

def store_docs():
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    table_name = config['table_name']
    host = config['hbase_host']
        
    connection = happybase.Connection(host)
    connection.open()
    # get table object
    table = connection.table(table_name)

    # traverse directory in "documents" folder, each subdirectory's name is the college name
    # each file in the subdirectory is a document
    # "documents" folder is in the same directory as this script
    curdir = os.path.dirname(__file__)
    for college in os.listdir(curdir+'/documents'):
        
        for filename in os.listdir(curdir+f'/documents/{college}'):
            # read file
            abspath = curdir+f'/documents/{college}/{filename}'
            data = doc_to_bytes(abspath)

            row_key = f'{college}_{filename}'.encode('utf-8')
            content = {b'info:filename': filename.encode('utf-8'), b'info:college': college.encode('utf-8'), b'data:data': data}
            # create put object
            put = table.put(row_key, content)

    connection.close()

if __name__ == '__main__':
    store_docs()