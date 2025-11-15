from flask import Flask, request, jsonify, render_template
from graph.build_graph import build_graph
from graph.state import ChatState

app = Flask(__name__, template_folder="templates")
graph = build_graph()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    state = ChatState(user_input=message)
    result = graph.invoke(state)
    if isinstance(result, dict):
        response_text = result.get("llm_response", "⚠️ No response generated.")
    else:
        response_text = getattr(result, "llm_response", "⚠️ No response generated.")

    return jsonify({"response": response_text})


graph = build_graph()


if __name__ == "__main__":
    app.run(debug=True)
