from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.config import settings
from app.core.logger import get_logger
from app.exceptions.custom_exceptions import agentError
from app.tools import tools

logger = get_logger(__name__)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    api_key=settings.GEMINI_API_KEY
)

# Agent
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt= "You must use tools to answer questions when possible.",
    debug=settings.VERBOSE
)

def run_agent(query: str) -> str:
    logger.info(f"Agent called with query: {query}")
    try:
        response = agent.invoke({
        "messages": [
            {"role": "user", "content": query}
        ]
    })
        return response["messages"][-1].content
    except Exception as e:
        logger.error("agent error", exc_info=True)
        raise agentError("fail to call agent", status_code=500) from e
