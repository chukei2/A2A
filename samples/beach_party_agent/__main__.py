import uvicorn

from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill

from .agent_executor import BeachPartyAgentExecutor


if __name__ == "__main__":
    skill = AgentSkill(
        id="plan_beach_party",
        name="Plan a beach party",
        description="Returns a simple beach party plan",
        tags=["party", "planning", "beach"],
        examples=["plan my beach party"],
    )

    public_agent_card = AgentCard(
        name="Beach Party Planner",
        description="Agent that helps plan a beach party",
        url="http://localhost:9999/",
        version="0.1.0",
        defaultInputModes=["text"],
        defaultOutputModes=["text"],
        capabilities=AgentCapabilities(streaming=True),
        skills=[skill],
        supportsAuthenticatedExtendedCard=False,
    )

    request_handler = DefaultRequestHandler(
        agent_executor=BeachPartyAgentExecutor(),
        task_store=InMemoryTaskStore(),
    )

    server = A2AStarletteApplication(
        agent_card=public_agent_card,
        http_handler=request_handler,
    )

    uvicorn.run(server.build(), host="0.0.0.0", port=9999)
