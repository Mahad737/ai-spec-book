import os
import markdown
from google import genai
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance

# =========================
# Gemini Client
# =========================
client_gemini = genai.Client(
    api_key=os.environ["GOOGLE_API_KEY"]
)

# =========================
# Qdrant Local Client
# =========================
qdrant = QdrantClient(path="./qdrant_data")

COLLECTION_NAME = "book_chapters"

# =========================
# Recreate Collection
# Gemini embedding size = 3072 ✅
# =========================
qdrant.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(
        size=3072,
        distance=Distance.COSINE
    )
)

# =========================
# Read & Ingest Markdown
# =========================
chapters_folder = "../docs"

point_id = 1  # ✅ integer ID ONLY

for filename in os.listdir(chapters_folder):
    if not filename.endswith(".md"):
        continue

    file_path = os.path.join(chapters_folder, filename)

    with open(file_path, "r", encoding="utf-8") as f:
        text = markdown.markdown(f.read())

    embedding = client_gemini.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    ).embeddings[0].values

    qdrant.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=point_id,
                vector=embedding,
                payload={
                    "text": text,
                    "source": filename
                }
            )
        ]
    )

    print(f"Ingested: {filename}")
    point_id += 1
