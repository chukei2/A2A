from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.utils import new_agent_text_message


class BeachPartyAgent:
    """Simple agent that returns a beach party plan."""

    async def invoke(self) -> str:
        return (
            "Beach Party Plan:\n"
            "1. Choose a date and time\n"
            "2. Prepare food and drinks\n"
            "3. Bring beach games\n"
            "4. Set up a sound system\n"
        )


class BeachPartyAgentExecutor(AgentExecutor):
    """AgentExecutor wrapping BeachPartyAgent."""

    def __init__(self) -> None:
        self.agent = BeachPartyAgent()

    async def execute(
        self, context: RequestContext, event_queue: EventQueue
    ) -> None:
        result = await self.agent.invoke()
        event_queue.enqueue_event(new_agent_text_message(result))

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        raise NotImplementedError("cancel not supported")
