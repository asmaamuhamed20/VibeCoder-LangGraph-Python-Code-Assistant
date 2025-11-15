from utils.llm_api import call_llm
from retriever.retriever import retrieve_examples

def chat_node(state):
    print("User:", state.user_input)
    return state

def router_node(state):
    text = state.user_input.lower()
    if any(k in text for k in ["gen", "generate", "create", "write", "make", "build"]):
        state.intent = "generate_code"
    elif any(k in text for k in ["explain", "describe", "what does", "meaning of"]):
        state.intent = "explain_code"
    else:
        state.intent = "generate_code"  
    print(f"🧭 Routed to: {state.intent}")
    return state


def generate_code_node(state):
    examples = retrieve_examples(state.user_input)
    state.retrieved_examples = examples
    state.llm_response = call_llm("generate", state.user_input, examples)
    return state

def explain_code_node(state):
    examples = retrieve_examples(state.user_input)
    state.retrieved_examples = examples
    state.llm_response = call_llm("explain", state.user_input, examples)
    return state
