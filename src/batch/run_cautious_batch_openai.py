import time
from pathlib import Path
from openai import OpenAI

def main():
    client = OpenAI()

    my_position = Path(__file__).resolve().parent
    root = my_position.parent.parent
    input_path = root / "processed_defan" / "cautious_defan_prompts.jsonl"
    output_folder = root / "openAI_responses"
    output_folder.mkdir(parents=True, exist_ok=True)
    output = output_folder / "cautious_defan_responses.jsonl"

    with input_path.open("rb") as f:
        batch_input_file = client.files.create(
            file=f,
            purpose="batch",
        )

    batch = client.batches.create(
        input_file_id=batch_input_file.id,
        endpoint="/v1/responses",
        completion_window="24h",
        metadata={"description": "cautious_defan batch"},
    )

    while True:
        batch = client.batches.retrieve(batch.id)
        status = batch.status
        if status == "completed":
            break
        # check status each hour, nice to see update
        time.sleep(3600)

    file_stream = client.files.content(batch.output_file_id)
    content = file_stream.read()
    output.write_bytes(content)

if __name__ == "__main__":
    main()