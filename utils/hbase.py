import happybase

class HbaseConnection:
    def __init__(self, host):
        self.connection = happybase.Connection(host)
        self.connection.open()
    
    def get_table(self, table_name):
        return self.connection.table(table_name)
    
    def close(self):
        self.connection.close()
    
    # ambigous search
    # TODO: I need to know what's the format of the query and search result
    def search_ambigous(self, table_name, columns, query, sort=True):
        table = self.get_table(table_name)
        result = []
        for key, data in table.scan(columns=columns):
            if query in data.values():
                result.append((key, data))
        
        if sort:
            # for each column, get an similarity score, using tf-idf with scikit-learn
            # then weight the score with each column considered
            # finally sort the result by score
            pass

        return result