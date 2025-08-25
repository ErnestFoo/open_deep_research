import asyncio
from open_deep_research.deep_researcher import deep_researcher, AgentInputState, Configuration

input_state = AgentInputState(messages=[...])  # Your initial user messages
config = {"configurable": Configuration(...)}  # Your config settings

result = asyncio.run(deep_researcher.ainvoke(input_state, config))
print(result)