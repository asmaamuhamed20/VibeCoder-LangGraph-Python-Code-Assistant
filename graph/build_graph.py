from langgraph.graph import StateGraph, END
from graph.state import ChatState
from graph.nodes import chat_node, router_node, generate_code_node, explain_code_node

def build_graph():
    graph = StateGraph(ChatState)

    graph.add_node("chat", chat_node)
    graph.add_node("router", router_node)
    graph.add_node("generate_code", generate_code_node)
    graph.add_node("explain_code", explain_code_node)

    graph.add_edge("chat", "router")
    graph.add_conditional_edges(
        "router",
        lambda s: s.intent,
        {
            "generate_code": "generate_code",
            "explain_code": "explain_code",
            "unknown": END
        }
    )

    graph.add_edge("generate_code", END)
    graph.add_edge("explain_code", END)
    graph.set_entry_point("chat")

    return graph.compile()
