
import chromadb
from chromadb.utils import embedding_functions


class MemoryService:

    def __init__(self):

        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )

        self.collection = self.client.get_or_create_collection(
            name="natasha_memory",
            embedding_function=self.embedding_fn
        )

    def add_memory(self, user_id: str, text: str, metadata: dict = None):

        self.collection.add(
            documents=[text],
            ids=[str(hash(text))],
            metadatas=[metadata or {"user_id": user_id}]
        )

    def search_memory(self, query: str, k: int = 3):

        results = self.collection.query(
            query_texts=[query],
            n_results=k
        )

        return results.get("documents", [[]])[0]


memory_service = MemoryService()
