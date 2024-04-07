from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
p = Path(__file__).parent


for i in range(10):
    files = p.glob("transcripts/*.txt")
    for file in files:
        time.sleep(1)
        print(f"Generating transcript for {file.name}, round {i+1}")
        with open(file) as rf, open(p / f"q-and-a/{file.stem}-{i+1}.txt", "w") as wf:
            transcript = rf.read()
            prompt = f"""
    Given the following transcript from a video, generate five questions and answers that provide instructions on appropriate social behaviors. The videos often use example of specific characters and situations, but the advice should be phrased as generalized answers to questions. DO NOT mention the characters in the videos, instead generalize the advice. You MUST maintain the original tone/personality of the speaker in the video and you MUST restrict all questions and answers to the content of the video. Each answer MUST be at least 250 words long, no shorter. The output should be in JSON format, as per the example.

    Example:
    [{{
        "question": "How can I be a good citizen?",
        "answer": "Being a good citizen involves doing little things for others and being considerate of those around you. You can start by helping your friends and classmates in small ways, such as tying their sash or helping them prepare for a lesson. It's also important to think ahead and be prepared, so you don't disturb others or cause trouble. During recess, you can play games that everyone can enjoy, and make sure to include others in your activities. Doing your job the best you can and taking pride in your work is also part of being a good citizen. Additionally, being careful and neat, and practicing good manners such as picking up after yourself and not holding up lines, are important habits to develop. As you grow older, these habits will become second nature and you will be seen as a considerate and responsible person."
    }},
    {{
        "question": "What are good table manners?",
        "answer": "1. Seating the girl: The gentleman should seat the lady first.\n2. Sitting: The gentleman should wait for the lady to be seated before sitting down.\n3. Ordering the meal: The gentleman should order his meal after the lady has ordered hers.\n4. Eating properly: The gentleman should eat with his knife and fork, using common sense and not making a mess.\n5. Finishing the meal: The gentleman should place his knife and fork in a specific way to show that he has finished eating.\n6. Handling spoon foods: The gentleman should dip the spoon away from himself when eating spoon foods, such as soup.\n7. Showing courtesy and consideration: The gentleman should show courtesy and consideration towards others, such as not tipping the bowl when eating soup and not eating too much from the spoon.\nIt is important to practice good table manners regularly at home so that they come naturally when dining out. Watching others with good manners, such as one's parents, can also be helpful in learning proper table etiquette. The main thing is to use common sense and be considerate of others, and good table manners will follow naturally."
    }}]


    TRANSCRIPT:
    {transcript}
    """
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
                max_tokens=4096,
                temperature=0.7,
            )
            wf.write(completion.choices[0].message.content)
