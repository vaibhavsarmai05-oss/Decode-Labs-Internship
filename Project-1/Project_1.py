print("="*40)
print("   Welcome to AI Chatbot")
print("="*40)
print("Type 'exit' or 'end' to stop\n")
response = {
    "hi": "Bot: Hello! What's up",
    "hello": "Bot: Hi! How are you",
    "all good" : "Bot: Nice",
    "i am fine" : "Bot: Good to hear that",
    "who are you": "Bot: I am a Rule-Based Chatbot",
    "help": "Bot: Try asking about AI , Python or Hi",
    "ai" : "Bot: Artificial Intelligence",
    "python" : "Bot: It is a programming language"
}
user = input("Bot: Ask me something: ")
while True:
    cleaned_user = user.lower().strip()
    if(cleaned_user == "exit" or cleaned_user == "end"):
        print("Bot: Thank you for chatting! Goodbye")
        print("="*40)
        break
    reply = response.get(cleaned_user, "Bot: Sorry! I don't understand it")
    print(reply)
    user = input("You: ")