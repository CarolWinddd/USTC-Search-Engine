import os

def doc_to_bytes(doc_path)->bytes:
    """
    Convert a document to bytes.
    """
    return open(doc_path, 'rb').read()

def bytes_to_doc(doc_bytes, doc_name, output_dir)->None:
    """
    Convert bytes to a document.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return open(f'{output_dir}/{doc_name}', 'wb').write(doc_bytes)
    
    
if __name__ == '__main__':
    doc = '大数据系统大作业实验文档.pdf'
    doc_bytes = doc_to_bytes(doc)
    
    # test bytes_to_doc, save into document_read folder, as a new file
    doc_name = 'test.pdf'
    output_dir = 'document_read'
    data = bytes_to_doc(doc_bytes, doc_name, output_dir)