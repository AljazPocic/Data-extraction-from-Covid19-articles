"""This is a prototype script for extracting data from a single
aricle. The real script will loop through multiple articles"""

from dotenv import load_dotenv
import os 

load_dotenv()
api_key = os.environ["GROQ_API_KEY"]



# Schema for extracting data
from pydantic import BaseModel, Field
from typing import List, Optional

class CovidData(BaseModel):
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



# Article
with open("articles/04_slovenia_konec_epidemije.txt", "r", encoding="utf-8") as file:
    article_text = file.read()
    header, body = article_text.split("---", maxsplit=1)  # sprem. body ima le vsebino članka, zato jo bom posredoval v prompt

prompt = (
    f"Extract the Covid_19 data from article wrapped in >><<: >>{body}<<"
    )



import instructor
from groq import Groq

client = instructor.from_groq(Groq(), mode=instructor.Mode.JSON)

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

# print the whole competion
print(f"\nExtracted Covid data: \n"
      f"{completion} \n")
# or print a specific data point
print(f"Number of infected: {completion.num_of_infected}")


# Store data in a dict or JSON-formatted string
data_dict = completion.model_dump()
data_json = completion.model_dump_json()
