# VibeCoder-LangGraph-Python-Code-Assistant

VibeCoder is an intelligent Python coding assistant built using LangGraph, Retrieval-Augmented Generation (RAG), ChromaDB, and OpenRouter.
It can generate and explain Python code professionally using a state-machine workflow and a clean Flask-based web interface.

START → classify_intent → route → (generate_code / explain_code) → END


. Retrieval-Augmented Generation (RAG)

The HumanEval dataset is loaded and embedded into ChromaDB.

At query time, semantically similar examples are retrieved.

Retrieved examples help the LLM produce more accurate and contextually relevant code.

3. LLM Integration (OpenRouter)

The system sends structured prompts to OpenRouter-supported models.
Keys are safely handled using environment variables.

4. Flask Web Interface

A simple UI is built using HTML, CSS, and JavaScript:

User and assistant chat bubbles

Code formatting with syntax highlighting

Supports Python code generation and explanation



Installation
1. Clone the project
git clone <https://github.com/asmaamuhamed20/VibeCoder-LangGraph-Python-Code-Assistant.git>
cd LangGraph_Code_Assistant
