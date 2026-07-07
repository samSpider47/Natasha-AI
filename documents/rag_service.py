
from documents.document_loader import document_loader
from documents.text_splitter import document_splitter
from documents.vector_store import vector_store


class RAGService:

    def index_document(
        self,
        uploaded_file
    ) -> bool:
        """
        Reads a PDF, splits it into chunks
        and stores it in ChromaDB.
        """

        text = document_loader.load_pdf(
            uploaded_file
        )

        chunks = document_splitter.split(
            text
        )

        return vector_store.add_document(
            uploaded_file.name,
            chunks
        )

    def has_documents(self) -> bool:
        """
        Returns True if at least one document
        has been indexed.
        """

        return vector_store.total_chunks() > 0

    def retrieve_context(
        self,
        query: str,
        k: int = 4
    ) -> str:

        return vector_store.similarity_search(
            query,
            k
        )

rag_service = RAGService()
