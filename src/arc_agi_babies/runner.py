from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.memory.in_memory_memory_service import InMemoryMemoryService
from google.genai import types
import uuid

from arc_agi_babies.utils import utils

async def run_task(agent, task):
    session_id = f"{agent.name}-session-{str(uuid.uuid4())}"
    runner = Runner(
        app_name=agent.name + "_app",
        agent=agent,
        session_service=InMemorySessionService(),
        memory_service=InMemoryMemoryService(),
    )
    session = await runner.session_service.create_session(
        app_name=agent.name,
        user_id='tmp_user',
        session_id=session_id,
    )

    content = types.Part.from_text(text=utils.task_to_text(task))
    print(f"Content: {content}")
    print(f"Session: {session}")

    last_event = None
    async for event in runner.run_async(user_id=session.user_id, session_id=session_id, new_message=content):
        print("hey")
        last_event = event
        print(last_event)

    return 0