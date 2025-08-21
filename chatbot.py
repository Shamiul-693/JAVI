import PyPDF2
from sentence_transformers import SentenceTransformer
import faiss
import os, json

PDF_PATH = "financial_policy.pdf"

# -------- PDF Parser --------
def parse_pdf(file_path):
    reader = PyPDF2.PdfReader(file_path)
    chunks, metadata = [], []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            for part in text.split(". "):
                if part.strip():
                    chunks.append(part.strip())
                    metadata.append(f"Page {i+1}")
    return chunks, metadata

# -------- Build / Load Index --------
def build_index():
    chunks, metadata = parse_pdf(PDF_PATH)
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks, convert_to_numpy=True)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    return model, index, chunks, metadata

model, index, chunks, metadata = build_index()

# -------- Chatbot --------
def ask(question):
    q_emb = model.encode([question], convert_to_numpy=True)
    D, I = index.search(q_emb, k=1)
    answers = []
    for idx in I[0]:
        answers.append(f"{chunks[idx]} ({metadata[idx]})")
    return answers

def chat():
    print("💬 Financial Policy Chatbot (type 'exit' to quit)")
    while True:
        q = input("You: ")
        if q.lower() in ["exit", "quit"]:
            break
        results = ask(q)
        print("\nBot:")
        for r in results:
            print("-", r)
        print()

if __name__ == "__main__":
    chat()
