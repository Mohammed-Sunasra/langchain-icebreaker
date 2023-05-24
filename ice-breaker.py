from dotenv import load_dotenv
load_dotenv()

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from external.linkedin import scrape_linkedin_profile
from agents.linkedin_agent import lookup as linkedin_lookup_agent

if __name__ == "__main__":
    print("Hello Langchain!")

    template = """
    Given the information about a person from LinkedIn {information}, I want you to create 
    1. A short summary
    2. two interesting facts about them
    """

    summary_template = PromptTemplate(input_variables=['information'], template=template)

    llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo')
    chain = LLMChain(llm=llm, prompt=summary_template)
    linkedin_profile_url = linkedin_lookup_agent(name="Rahul Jain Pixeldust")
    linked_in_data = scrape_linkedin_profile(linkedin_profile_url)

    print(chain.run(information=linked_in_data))