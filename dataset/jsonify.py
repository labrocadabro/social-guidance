from pathlib import Path
from collections import defaultdict
import json

p = Path(__file__).parent

in_path = p / "q-and-a"
out_path = p / "json"

# Dictionary to store files grouped by base name
file_groups = defaultdict(list)

files = in_path.glob("*.txt")

# Iterate over each file in the folder
for file in files:
    base_name = file.stem.split("-")[0]  # Extract the base name
    file_groups[base_name].append(file)

# print(file_groups)

for base_name, files in file_groups.items():
    print(f"Files with base name '{base_name}'")
    with open(out_path / f"{base_name}.json", "w") as wf:
        result = []
        for file_path in files:
            print(file_path)
            with open(file_path) as rf:
                text = rf.read()
                if text.startswith("```json"):
                    text = text[7:-3]
                file_json = json.loads(text)
                result += file_json
        wf.write(json.dumps(result))
