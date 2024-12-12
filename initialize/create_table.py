import happybase
import json


def create_table():
    with open('config.json', 'r') as f:
        config = json.load(f)
        print(config)
    exit()
    table_name = config['table_name']
    column_families = {k: dict() for k in config['column_families']}
    host = config['hbase_host']

    connection = happybase.Connection(host)
    connection.open()

    # create table if not exists
    if table_name not in connection.tables():
        connection.create_table(
            table_name,
            column_families
        )

    connection.close()