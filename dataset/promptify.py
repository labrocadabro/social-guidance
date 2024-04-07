from pathlib import Path
from collections import defaultdict
import json

p = Path(__file__).parent

in_path = p / "json"
out_path = p / "prompts"

file_groups = defaultdict(list)

files = in_path.glob("*.json")

# Iterate over each file in the folder
for file in files:
    print(file)
    with open(file) as rf, open(out_path / f"{file.stem}.txt", "w") as wf:
        print(file)
        text = rf.read()
        file_json = json.loads(text)
        for item in file_json:
            prompt = f"<s>[INST] <<SYS>>\\nYou are a helpful assistant answering questions about social behavior.\\n<</SYS>>\\n\\n{item['question']} [/INST] {item['answer']} </s>\n"
            wf.write(prompt)
