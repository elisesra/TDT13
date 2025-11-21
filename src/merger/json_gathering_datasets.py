import json
from pathlib import Path

JSON_FILES = [
    "../../DefAn/DefAn-public/QA_domain_1_public.json",
    "../../DefAn/DefAn-public/QA_domain_2_public.json",
    "../../DefAn/DefAn-public/QA_domain_3_public.json",
]

def main():
    my_position = Path(__file__).resolve().parent
    output = my_position / "correct_10k_public.json"

    merged = []

    for filename in JSON_FILES:
        if len(merged) >= 10_000:
            break

        path = my_position / filename

        with path.open("r", encoding="utf-8") as f:
            dataset = json.load(f)
        for sets in dataset:
            if len(merged) >= 10_000:
                break

            question = sets.get("questions")
            answr = sets.get("answer")
            custom_id = f"row-{len(merged)}"

            merged.append({
                "custom_id": custom_id,
                "questions": question,
                "answers": answr,
            })

    with output.open("w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()