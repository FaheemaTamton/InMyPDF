from ingestion.text_ingest import extract_text
from ingestion.table_ingest import extract_tables
from ingestion.image_ingest import extract_images_text
from rag.text_splitter import split_text
from rag.vector_store import create_store
from agent.agent import create_agent

agent = create_agent()


def process_pdf(pdf_file):
    # Save file temporarily
    file_path = f"temp_{pdf_file.filename}"
    with open(file_path, "wb") as f:
        f.write(pdf_file.read())

    text = extract_text(file_path)
    tables = extract_tables(file_path)
    images = extract_images_text(file_path)

    combined_text = f"""
    TEXT CONTENT:
    {text}

    TABLE CONTENT:
    {tables}

    IMAGE CONTENT:
    {images}
    """

    chunks = split_text(combined_text)
    create_store(chunks)
    return True


def answer_query(_, question: str):
    return agent.run(question)
