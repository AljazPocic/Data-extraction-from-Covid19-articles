"""This file is meant for extracting Covid-19 data by looping through 
multiple files."""

from schema import CovidData
import instructor
from groq import Groq, RateLimitError
from pathlib import Path
import time

from dotenv import load_dotenv
import os 

load_dotenv()
api_key = os.environ["GROQ_API_KEY"]


client = instructor.from_groq(Groq(), mode=instructor.Mode.JSON)


def extract_from_article(file_path):
    """Fun meant to extract data from article"""

    with open(f"{file_path}", "r", encoding="utf-8") as file:
        article_text = file.read()
        header, body = article_text.split("---", maxsplit=1)  # sprem. body ima le vsebino članka, zato jo bom posredoval v prompt

    prompt = (
        f"Extract the Covid_19 data from article wrapped in >><<: >>{body}<<"
        )

    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        response_model=CovidData,  # the Pydantic class
        messages=[
          {
            "role": "user", # Think of as "Who is speaking?", Anwser: User
            "content": prompt
          }
        ],
        temperature=0,
        max_completion_tokens=2048,
        top_p=1,
        reasoning_effort="medium",
        stop=None,
        max_retries=3

    )

    return completion


if __name__ == "__main__":
    artices_dir = Path("articles")

    data = {}  # data for all the articles will be appended to this dict

    max_attempts = 3

    for article_path in sorted(artices_dir.glob("*.txt")):
        for attempt in range(1, max_attempts + 1):
            try:
                data[article_path.stem] = extract_from_article(article_path)
                print(f"{article_path.stem} data added to dict.")
                time.sleep(3)
                break  # if succesful exit the nested loop
            except RateLimitError as e:
                print(f"Attempt {attempt} faild. Reason: {e}")
                if attempt == max_attempts:
                    data[article_path.stem] = None
                else:
                    print("Trying again")
                    time.sleep(3)


# Run "python3 -i extraxt_all.py" in terminal and try some commands like:
# data['11_slovenia'], data['11_slovenia'].model_dump()...