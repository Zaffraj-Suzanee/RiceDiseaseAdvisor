from typing import TypedDict, List


class AgentMessage(TypedDict):

    sender: str
    receiver: str
    task: str
    content: dict
    status: str