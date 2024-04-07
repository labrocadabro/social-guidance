from pathlib import Path
from collections import defaultdict
import json

p = Path(__file__).parent

in_path = p / "json"

file_groups = defaultdict(list)

files = in_path.glob("*.json")

questions = []

for file in files:
    with open(file) as rf:
        print(file)
        text = rf.read()
        file_json = json.loads(text)
        for item in file_json:
            questions.append(item["question"])


with open(p / "questions.txt", "w") as wf:
    wf.write(json.dumps(questions))
