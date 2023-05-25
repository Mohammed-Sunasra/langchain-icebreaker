from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from external.linkedin import scrape_linkedin_profile
from external.twitter import scrape_user_tweets
from agents.linkedin_agent import lookup as linkedin_lookup_agent
from output_parser import person_intel_parser

if __name__ == "__main__":
    print("Hello Langchain!")

    template = """
    Given the LinkedIn information {information} about a person, I want you to create:
    1. A short summary
    2. two interesting facts about them
    3. A topic that may interest them
    4. 2 Creative ice breakers to open a conversation with them
    \n{format_instructions}
    """

    summary_template = PromptTemplate(input_variables=['information'], 
                                      template=template, 
                                      partial_variables={"format_instructions": person_intel_parser.get_format_instructions()}
                                      )

    llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo')
    chain = LLMChain(llm=llm, prompt=summary_template)
    linkedin_profile_url = linkedin_lookup_agent(name="Rahul Jain Pixeldust")
    linked_in_data = scrape_linkedin_profile(linkedin_profile_url)

    result = chain.run(information=linked_in_data)
    print(result)
    print("-" * 100)
    parsed_response = person_intel_parser.parse(result)
    print("-" * 100)
    print(type(parsed_response))
    print(parsed_response)
    print("-" * 100)
    print(dict(parsed_response).keys())
    #print(scrape_user_tweets("@elonmusk"))