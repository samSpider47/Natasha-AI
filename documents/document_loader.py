
from pathlib import Path

from pypdf import PdfReader


class DocumentLoader:
    """
    Responsible for reading uploaded PDF files
    and extracting their text.
    """

    def load_pdf(self, uploaded_file) -> str:

        try:

            reader = PdfReader(uploaded_file)

            pages = []

            for page in reader.pages:

                text = page.extract_text()

                if text:
                    pages.append(text)

            return "\n".join(pages)

        except Exception as e:

            raise Exception(
                f"Unable to read PDF: {e}"
            )


document_loader = DocumentLoader()
