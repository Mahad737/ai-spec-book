import os
import time
from google import genai
from google.genai.errors import ClientError, ServerError
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

# =========================
# Gemini Client
# =========================
client_gemini = genai.Client(
    api_key=os.environ.get("GOOGLE_API_KEY")
)

# =========================
# Qdrant Local Client
# =========================
qdrant = QdrantClient(path="./qdrant_data")
COLLECTION_NAME = "book_chapters"

# =========================
# Helper: Get Embedding
# =========================
def get_embedding(text: str):
    response = client_gemini.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )
    return response.embeddings[0].values

# =========================
# Search in Qdrant
# =========================
def search_book(query: str, limit: int = 3):
    query_vector = get_embedding(query)

    results = qdrant.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=limit
    )

    return results

# =========================
# Generate Answer (RAG)
# =========================
def answer_question(question: str):
    results = search_book(question)

    if not results:
        return "Answer not available in the book."

    # Build context from top results
    context = ""
    for r in results:
        context += f"\n---\nSource: {r.payload.get('source','Unknown')}\n{r.payload.get('text','')}\n"

    prompt = f"""
You are an AI assistant answering strictly from the provided book content.

Book Content:
{context}

Question:
{question}

Rules:
- Answer ONLY from the book content
- If answer is not found, say: "Answer not available in the book."
- Keep answer clear and concise
"""

    # =========================
    # Call Gemini with retries
    # =========================
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client_gemini.models.generate_content(
                model="gemini-2.5-pro",
                contents=prompt
            )
            return response.text  # ✅ return inside function
        except ClientError as e:
            if "RESOURCE_EXHAUSTED" in str(e):
                return "Quota exhausted! Please check your API key and billing."
            else:
                print(f"Client error: {e}, retrying...")
        except ServerError as e:
            print(f"Server busy: {e}, retrying in 5s...")
            time.sleep(5)
    return "Failed to get answer from AI after multiple attempts."

# =========================
# CLI Entry Point
# =========================
if __name__ == "__main__":
    print("📘 AI Book RAG Chatbot")
    print("Type 'exit' to quit\n")

    while True:
        user_question = input("❓ Ask from book: ")
        if user_question.lower() == "exit":
            break

        answer = answer_question(user_question)
        print("\n💡 Answer:\n", answer)
        print("\n" + "="*50 + "\n")
