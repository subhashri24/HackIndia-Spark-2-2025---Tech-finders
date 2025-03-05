import chromadb

chroma_client = chromadb.PersistentClient(path="./chromadb_store")
collection = chroma_client.get_collection("faq_collection")

query = input("Ask your coding question: ")

results = collection.query(
    query_texts=[query],
    n_results=3
)

print(" Top Matches:")
for result in results["documents"][0]:
    print(result)
