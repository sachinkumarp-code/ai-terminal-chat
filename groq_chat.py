from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

conversation_history = []

print("Groq AI Chat — type 'quit' to exit\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "quit":
        print("Bye!")
        break
    
    conversation_history.append({
        "role": "user",
        "content": user_input
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
