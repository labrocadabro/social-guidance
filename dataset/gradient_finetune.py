from dotenv import load_dotenv
from gradientai import Gradient
from pathlib import Path


load_dotenv()

p = Path(__file__).parent / "prompts-2"

files = p.glob("*.txt")


gradient = Gradient()

model_adapter = gradient.get_model_adapter(
    model_adapter_id="d212e88b-60db-4701-a8ec-418bad184536_model_adapter"
)

for file in files:
    with open(file) as f:
        lines = f.read().splitlines()
        samples = [{"inputs": line} for line in lines]
        print(f"fine tuning with {file}")
        model_adapter.fine_tune(samples=samples)
gradient.close()
