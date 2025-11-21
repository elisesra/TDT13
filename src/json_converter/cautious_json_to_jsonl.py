import json
from pathlib import Path

FILES = [
    "../../DefAn/DefAn-public/QA_domain_1_public.json",
    "../../DefAn/DefAn-public/QA_domain_2_public.json",
    "../../DefAn/DefAn-public/QA_domain_3_public.json",
]

def main():
    my_position = Path(__file__).resolve().parent 
    output_folder = my_position.parent.parent/ "processed_defan"
    output_folder = my_position.parent.parent / "processed_defan"
    output_folder.mkdir(parents=True, exist_ok=True)
    out_path = output_folder / "cautious_defan_prompts.jsonl"

    prompts = []
    for QA_file in FILES:

        if len(prompts) >= 10_000:
            break

        with (my_position / QA_file).open("r", encoding="utf-8") as file:
            dataset = json.load(file)

        for sets in dataset:
            if len(prompts) >= 10_000:
                break

            question_line = sets.get("questions")
            if isinstance(question_line, str):
                prompts.append(question_line)
            elif isinstance(question_line, list):
                for row in question_line:
                    if len(prompts) >= 10_000:
                        break
                    prompts.append(str(row))

    cautious = "Answer like a cautious assistant: "

    with out_path.open("w", encoding="utf-8") as f:
        for i, prompt in enumerate(prompts):
            line = {
                "custom_id": f"row-{i}",
                "method": "POST",
                "url": "/v1/responses",
                "body": {
                    "model": "gpt-4.1-nano",
                    "input": cautious+prompt,
                },
            }
            f.write(json.dumps(line, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    main()
