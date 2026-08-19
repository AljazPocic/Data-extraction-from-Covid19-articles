"""This file is ment for extracting Covid-19 data by looping through 
multiple files."""

from schema import CovidData
import instructor
from groq import Groq
from pathlib import Path

from dotenv import load_dotenv
import os 

load_dotenv()
api_key = os.environ["GROQ_API_KEY"]



client = instructor.from_groq(Groq(), mode=instructor.Mode.JSON)


def extract_from_article(file_path):
    """Fun ment to extract data from article"""

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
        stop=None
    )

    return completion


if __name__ == "__main__":
    artices_dir = Path("articles")

    data = []  # data for all the articles will be appended to this list

    for article_path in sorted(artices_dir.glob("*.txt")):
        article_data_dict = {article_path.stem: extract_from_article(article_path)}
        data.append(article_data_dict)
        print(f"{article_path.stem} data added to list.")

