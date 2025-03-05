import chromadb
import json

# Create ChromaDB Client
chroma_client = chromadb.PersistentClient(path="./chromadb_store")

# Create Collection
collection = chroma_client.get_or_create_collection("faq_collection")

# Load Dataset
with open("faq_dataset.json") as file:
    faqs = json.load(file)

# Insert FAQs into ChromaDB
for faq in faqs:
    collection.add(
        documents=[faq["answer"]],
        metadatas={"question": faq["question"]},
        ids=[faq["question"]]
    )

print(f" {len(faqs)} FAQs Successfully Stored in ChromaDB")
