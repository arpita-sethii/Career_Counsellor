# chatbot_logic.py

from langchain_community.llms import Ollama
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

# Load local LLM (Gemma)
llm = Ollama(model="gemma:2b")

# Wikipedia tool
wikipedia = WikipediaAPIWrapper(top_k_results=2)
tools = [
    Tool(
        name="WikipediaSearch",
        func=wikipedia.run,
        description="Useful for fetching details about a college, course, or exam from Wikipedia"
    )
]

# System prompt
system_prompt = """
You are Arpita's personal AI assistant and career counselor.
Be friendly, emotionally aware, and helpful.
If asked about a college, course, entrance exam, or scholarship, search Wikipedia.
Otherwise, respond directly with your own advice.
"""

# Prompt template (for direct LLM responses)
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

# Agent (Gemma + Tools)
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True,
    max_iterations=8,
    max_execution_time=60
)

# Helper: Decide if Wikipedia is needed
def needs_search(query: str) -> bool:
    keywords = ["college", "university", "iit", "nit", "jee", "neet", "exam", "rank", "cutoff", "admission", "scholarship", "placement"]
    return any(word in query.lower() for word in keywords)

# Main chatbot response function
def get_chatbot_response(user_query: str) -> str:
    try:
        if needs_search(user_query):
            return agent.run(user_query)
        else:
            return llm.invoke(f"You are a warm, friendly career counselor. {user_query}")
    except Exception as e:
        return f"Oops! Something went wrong. Here's a direct response:\n\n{llm.invoke(user_query)}"
