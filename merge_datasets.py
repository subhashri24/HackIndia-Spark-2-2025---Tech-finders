import json

files = ["dataset/coding_faq.json", "dataset/stackoverflow_faq.json", "dataset/manual_faq.json"]
final_dataset = []

for file in files:
    with open(file, "r") as f:
        data = json.load(f)
        final_dataset.extend(data)

with open("dataset/final_dataset.json", "w") as outfile:
    json.dump(final_dataset, outfile, indent=4)

print(f" Final Dataset with {len(final_dataset)} FAQs Collected")
