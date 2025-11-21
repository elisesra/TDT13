import sys
import csv
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel 
from torch import Tensor

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-base")
model = AutoModel.from_pretrained("facebook/bart-base")


def embed(text: str) -> Tensor:
    encoded = tokenizer(
        text or "",
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128,
    )

    with torch.no_grad():
        out = model(**encoded)
        hidden = out.last_hidden_state 

    mask = encoded["attention_mask"].unsqueeze(-1) 
    masked = hidden * mask
    summed = masked.sum(dim=1)
    counts = mask.sum(dim=1).clamp(min=1)
    emb = summed / counts
    emb = F.normalize(emb, p=2, dim=1)
    return emb[0]


def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, newline="", encoding="utf-8") as ingoing, \
         open(output_path, "w", newline="", encoding="utf-8") as outgoing:

        reader = csv.DictReader(ingoing)
        fieldnames = list(reader.fieldnames) + ["bart_similarity"]
        writer = csv.DictWriter(outgoing, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            gold = row.get("gold_answer", "")
            model_ans = row.get("model_answer", "")

            embedding_vector_gold = embed(gold)
            embedding_vector_model = embed(model_ans)
            sim = torch.dot(embedding_vector_gold, embedding_vector_model).item()

            row["bart_similarity"] = f"{sim:.6f}"
            writer.writerow(row)


if __name__ == "__main__":
    main()
