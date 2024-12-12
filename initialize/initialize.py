from create_table import create_table
from store_docs import store_docs

def initialize():
    create_table()
    store_docs()

if __name__ == '__main__':
    initialize()