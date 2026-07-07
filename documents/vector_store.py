import hashlib
import uuid

import chromadb
from chromadb.utils import embedding_functions


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.embedding_function = (
            embedding_functions.SentenceTransformerEmbeddingFunction(
                model_name="all-MiniLM-L6-v2"
            )
        )

        self.collection = self.client.get_or_create_collection(
            name="documents",
            embedding_function=self.embedding_function
        )

    # ----------------------------------------------------
    # Private Helpers
    # ----------------------------------------------------

    def _document_hash(
        self,
        chunks: list[str]
    ) -> str:
        """
        Creates a fingerprint for the document.
        """

        text = "".join(chunks)

        return hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

    # ----------------------------------------------------
    # Public API
    # ----------------------------------------------------

    def add_document(
        self,
        document_name: str,
        chunks: list[str]
    ) -> bool:
        """
        Adds a document to ChromaDB.

        Returns
        -------
        True
            Newly indexed.

        False
            Already exists.
        """

        doc_hash = self._document_hash(chunks)

        existing = self.collection.get(
            where={
                "document_hash": doc_hash
            }
        )

        if existing["ids"]:
            return False

        ids = []
        documents = []
        metadatas = []

        for index, chunk in enumerate(chunks):

            ids.append(str(uuid.uuid4()))

            documents.append(chunk)

            metadatas.append(
                {
                    "document": document_name,
                    "document_hash": doc_hash,
                    "chunk": index
                }
            )

        self.collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )

        return True

    def list_documents(self) -> list[str]:
        """
        Returns all indexed document names.
        """

        data = self.collection.get()

        names = set()

        if data["metadatas"]:
            for meta in data["metadatas"]:
                if meta and "document" in meta:
                    names.add(meta["document"])

        return sorted(names)

    def total_chunks(self) -> int:

        return self.collection.count()

    def clear(self):

        self.client.delete_collection(
            "documents"
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="documents",
                embedding_function=self.embedding_function
            )
        )

    def similarity_search(
        self,
        query: str,
        k: int = 4
    ) -> str:

        results = self.collection.query(
            query_texts=[query],
            n_results=k
        )

        if not results["documents"] or not results["documents"][0]:
            return ""

        context = []

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        for doc, meta in zip(documents, metadatas):
            block = "\n".join([
                "",
                "======================================",
                "",
                f"Document : {meta['document']}",
                "",
                f"Chunk : {meta['chunk']}",
                "",
                f"{doc}",
                ""
            ])
            context.append(block)

        return "\n".join(context)


vector_store = VectorStore()
