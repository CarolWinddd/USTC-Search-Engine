# Hbase-based USTC Document Retrieval System with GUI

## Framework
This project is done almost fully with python. Library Happybase and PyQt5 are used to deal with hbase and user interaction (with GUI), respectively.

## Functions
1. Documents from USTC official websites can be stored in database.
2. Documents retrieval through some specific attributes is supported, according to how the table is designed, which will be mentioned in next part.
3. The result of retrieval is listed according to the similarity between the document and the search word. And it could be opened directly through GUI if you want.

## Details
1. Now, the table is designed as follow:

   |row_key|{filename}_{college}|
   |:-:|:-:|
   |info:filename|{filename}|
   |info:college|{college}|
   |data:bytes|{document in binary form}|

2. When retrieving, filename and and college will be taken into consideraion as raw_key is designed to contain them both.


# TODO
1. config.jsonhbase host and other configurations
2. utils.hbase: format of query and result
3. Docs to collect

2024.12.12 v1.0:\
Till now, all code is written in Windows. While 1.2. need to test in Linux