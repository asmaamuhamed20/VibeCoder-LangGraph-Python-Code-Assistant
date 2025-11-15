import chromadb
from chromadb.utils import embedding_functions
from datasets import load_dataset




client = chromadb.Client()

embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

collection = client.get_or_create_collection(
    name="humaneval",
    embedding_function=embed_fn
)


# Load dataset ONCE (only if empty)
if collection.count() == 0:
    print("🟡 Loading HumanEval dataset into ChromaDB...")
    dataset = load_dataset("openai/openai_humaneval", split="test")

    for idx, row in enumerate(dataset):
        collection.add(
            documents=[row["prompt"]],
            metadatas=[{"task_id": row["task_id"]}],
            ids=[str(idx)]
        )

    print("HumanEval dataset embedded and stored!")

else:
    print(" ChromaDB already contains HumanEval dataset.")


#  RETRIEVAL FUNCTION

def retrieve_examples(query: str):
    """Retrieve top similar examples from ChromaDB using embeddings (fast)."""

    results = collection.query(
        query_texts=[query],
        n_results=2
    )

    docs = results["documents"][0]

    return [{"code": doc} for doc in docs]
