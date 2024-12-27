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
    def search_ambigous(self, table_name, columns, query, sort=True):
        # import jieba
        table = self.get_table(table_name)
        documents = []
        result = {}
        # import time
        # t = time.time()
        for key, data in table.scan():
            college = data[b'info:college'].decode('utf-8')
            filename = data[b'info:filename'].decode('utf-8')
            if query in college or query in filename:
                documents.append(key)
                result[key] = [filename, college, data[b'data:data']]

        # print('search time:', time.time()-t) 
        if sort:
            from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
            from sklearn.metrics.pairwise import cosine_similarity
            # for each column, get an similarity score, using tf-idf with scikit-learn
            # finally sort the result by score
            tfidf = TfidfVectorizer()
            # tfidf = CountVectorizer()
            all_docs = [query]+documents
            tfidf_matrix = tfidf.fit_transform(all_docs)
            # print('trans time:', time.time()-t)
            similarity_matrix = cosine_similarity(tfidf_matrix)
            sort_result = {}
            for i in range(1, len(similarity_matrix)):
                sort_result[all_docs[i]] = similarity_matrix[0][i]
            sort_result = dict(sorted(sort_result.items(), key=lambda x: x[1], reverse=True))
            
            result = [(k, *result[k]) for k in sort_result.keys()]
        return result