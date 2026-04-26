from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from app.tools import tools
from app.core.logger import get_logger
from app.exceptions.custom_exceptions import agentError

logger = get_logger(__name__)

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
    logger.info(f"Agent called with query: {query}")
    try:
        response = agent.invoke({
        "messages": [
            {"role": "user", "content": query}
        ]
    })
        return response
    except Exception as e:
        logger.error("agent error", exc_info=True)
        raise agentError("fail to call agent") from e
