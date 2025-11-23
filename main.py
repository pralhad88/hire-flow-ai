from llama_index.core import VectorStoreIndex
from llama_index.core.retrievers import QueryFusionRetriever

from core.document_processing import document_processing
from core.embedding import llm_model_embedding

# Config file that contains secrets values and some hard coded values
from config import QUERY_RETRIEVER_MODEL


def main(query):
    docs = document_processing()
    print(f"Loaded {len(docs)} documents.")

    # Embed llm and embeded model with Google gemin.
    setting = llm_model_embedding()

    # Rebuild indexes with Gemini embeddings
    print("\n Building indexes with production Gemini embeddings...")
    vector_idx = VectorStoreIndex.from_documents(docs)
    
    # Create base retriever
    base_retriever = vector_idx.as_retriever(similarity_top_k=5)

    # QueryFusionRetriever automatically generates query variations
    fusion_retriever = QueryFusionRetriever(
        retrievers=[base_retriever],
        similarity_top_k=5,
        num_queries=3,
        mode=QUERY_RETRIEVER_MODEL,
        use_async=False,
        llm=setting.llm
    )

    multi_results = fusion_retriever.retrieve(query)

    print(multi_results)

if __name__ == "__main__":
    query = input("Enter Your Query:- ")
    main(query)
