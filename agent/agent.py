from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType

from agent.tools import retrieval_tool


def create_agent():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    agent = initialize_agent(
        tools=[retrieval_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent
