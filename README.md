# AI Terminal Chat

A conversational AI assistant that runs directly in the terminal,
built using the Groq API and Python.

## What it does
- Chat with an AI model (LLaMA 3.3 70B) from your terminal
- Maintains full conversation history within a session
- Launches from anywhere with a single command (gchat)
- Extremely fast responses powered by Groq's inference engine

## Tech used
- Python 3.13
- Groq API (llama-3.3-70b-versatile model)
- Shell scripting (zsh alias, environment variables)

## How to run
1. Clone this repo
2. Install dependency: pip install groq
3. Set your API key: export GROQ_API_KEY="your_key"
4. Run: python3 groq_chat.py

## Why I built this
Built this as a hands-on project to learn API integration,
Python scripting, and terminal tooling from scratch.
