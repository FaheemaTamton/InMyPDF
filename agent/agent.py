

    agent = initialize_agent(
        tools=[retrieval_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    return agent
