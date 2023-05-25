from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

class PersonIntel(BaseModel):
    summary: str = Field(description="Summary of the person")
    facts: str = Field(description="Interesting facts of the person")
    topics_of_interest: str = Field(description="Topics that may interest the person")
    ice_breakers: str = Field(description="Ice breakers to use when you meet or talk to the person")


    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "topics_of_interest": self.topics_of_interest,
            "ice_breakers": self.ice_breakers
        }
    
person_intel_parser = PydanticOutputParser(pydantic_object=PersonIntel)