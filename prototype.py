"""This is a protoype script for extracting data from a single
aricle. The real script will loop through multiple articles"""

from dotenv import load_dotenv
import os 

load_dotenv()
api_key = os.environ["GROQ_API_KEY"]


# Schema for extracting data
from pydantic import BaseModle, Field
from typing import List, Optional


class CovidData(BaseModle):
    location: str = Field(description="The city, region, or area affected")
    number_of_deaths: int = Field(
        description="The number of people dead, beacuse of Covid-19"
        )
    num_of_infected: int = Field(
        description="The number of people infected or sick beacuse of Covid-19"
        )
    num_recovered: Optional[int] = Field(
        default=None, description="The number of people who recoverd from being" \
        "sick with Covid-19"
    )
    list_of_measures: Optional[List[str]] = Field(
        default=None,
        description="List of measures taken to slow the spread of the Covid-19 virus"
    )




with open("articles/01_china_coronavirus_goes_global.txt", "r", encoding="utf-8") as file:
    article_text = file.read()

prompt = (
    f"Read the article wraped in >><<. Return data about location, number of deaths, "
    f"number of sick with covid-19 in JSON. If any of the date is not listed then give it the value None"
    f">>{article_text}<<"
)

from groq import Groq

client = Groq()
completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
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
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
