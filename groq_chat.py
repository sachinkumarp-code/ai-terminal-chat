from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

conversation_history = []

print("Groq AI Chat — type 'quit' to exit")
print("Tip: type 'read filename.py' to ask AI about a file\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Bye!")
        break

    # Check if user wants to read a file
    if user_input.lower().startswith("read "):
        filename = user_input[5:].strip()
        if os.path.exists(filename):
            with open(filename, "r") as f:
                file_content = f.read()
            message = f"Here is the file '{filename}':\n\n{file_content}\n\nPlease analyze this."
            print(f"[Reading {filename} and sending to AI...]\n")
        else:
            print(f"[File '{filename}' not found]\n")
            continue
    else:
        message = user_input

    conversation_history.append({
        "role": "user",
        "content": message
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history
    )

    reply = response.choices[0].message.content

    conversation_history.append({
        "role": "assistant",
        "content": reply
    })

    print(f"AI: {reply}\n")
