from dotenv import load_dotenv

load_dotenv()
from gradientai import Gradient


gradient = Gradient()


model_adapter = gradient.get_model_adapter(
    model_adapter_id="d212e88b-60db-4701-a8ec-418bad184536_model_adapter"
)

while True:
    query = input("What do you want to ask? (q to quit)\n")

    if query == "q":
        break

    completion = model_adapter.complete(
        query=query,
        max_generated_token_count=500,
        rag={"collection_id": "41f09e43-aaa2-42a8-b995-567fb72ab497_rag_config"},
    ).generated_output
    print(f"Generated: {completion}")


gradient.close()
