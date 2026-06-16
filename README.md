# AI Terminal Chat

A conversational AI assistant that runs directly in the terminal, 
built using the Google Gemini API and Python.

## What it does
- Chat with an AI model from your terminal
- Maintains conversation history within a session
- Launches from anywhere with a single command (gchat)

## Tech used
- Python 3.13
- Google Gemini API (gemini-1.5-flash)
- Shell scripting (zsh alias, environment variables)

## How to run
1. Clone this repo
2. Install dependency: pip install google-generativeai
3. Set your API key: export GEMINI_API_KEY="your_key"
4. Run: python3 gemini_chat.py
