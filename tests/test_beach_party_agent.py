import os
import sys
import pytest

# Ensure the root of the repository is on the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from samples.beach_party_agent.agent_executor import BeachPartyAgent


@pytest.mark.asyncio
async def test_beach_party_plan():
    agent = BeachPartyAgent()
    result = await agent.invoke()
    assert "Beach Party Plan" in result
