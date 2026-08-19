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