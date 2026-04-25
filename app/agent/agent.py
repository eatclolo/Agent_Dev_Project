from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from app.tools import tools

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# Agent
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt= "You must use tools to answer questions when possible.",
    debug=True
)

def run_agent(query: str) -> str:
    response = agent.invoke({
    "messages": [
        {"role": "user", "content": query}
    ]
})
    return response
