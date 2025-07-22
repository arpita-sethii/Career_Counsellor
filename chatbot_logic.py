# chatbot_logic.py

from langchain_community.llms import Ollama
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory

# Load local LLM (Gemma)
llm = Ollama(model="gemma:2b")

# Define system prompt
system_prompt = """
You are Arpita's personal AI assistant and career counselor.

Your responsibilities:
- Answer student questions clearly and emotionally if needed.
- Explain details about colleges, fees, entrance exams, placements, rankings, hostels.
- Comfort users if they sound stressed or emotional.
- Use Wikipedia to fetch fresh or unclear data.
"""

# Wikipedia search tool
wikipedia = WikipediaAPIWrapper(top_k_results=2)
tools = [
    Tool(
        name="WikipediaSearch",
        func=wikipedia.run,
        description="Useful for fetching details about a college, course, or exam from Wikipedia"
    )
]

# Memory: Keeps prior interactions
memory = ConversationBufferMemory(
    memory_key="chat_history",  # Mandatory key name for agent memory
    return_messages=True
)

# Agent with memory
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True,
    memory=memory
)

# Callable function for Streamlit to get response
def get_chatbot_response(user_query: str) -> str:
    return agent.run(user_query)
