from llama_index.core import SimpleDirectoryReader

def document_processing():

    docs = SimpleDirectoryReader(
        input_dir="./resume", required_exts=[".pdf"]
    ).load_data()

    return docs
