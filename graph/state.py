from pydantic import BaseModel
from typing import Literal, List, Optional

class ChatState(BaseModel):
    user_input: str
    intent: Literal["generate_code", "explain_code", "unknown"] = "unknown"
    retrieved_examples: Optional[List[dict]] = []
    llm_response: str = ""
