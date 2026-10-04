# Python Programming Assignment 2
# Task 2: Professional Text-Based Chatbot


def chatbot():

    print("================================================")
    print("              PYTHON AI CHATBOT")
    print("================================================")
    print("Bot: Hello! I am PythonBot, your virtual assistant.")
    print("Bot: You can ask me simple questions.")
    print("Bot: Type 'bye' anytime to end the conversation.")
    print("================================================")

    while True:

        user_message = input("\nYou: ").lower().strip()

        # 1. Greeting
        if user_message in ["hello", "hi", "hey", "assalam o alaikum"]:
            print("Bot: Hello! It is nice to talk to you. How can I help you?")

        # 2. Asking the bot's name
        elif "your name" in user_message or "who are you" in user_message:
            print("Bot: My name is PythonBot. I am a simple text-based virtual assistant.")

        # 3. Asking how the bot is
        elif "how are you" in user_message:
            print("Bot: I am doing great! Thank you for asking.")

        # 4. Asking what the bot can do
        elif "what can you do" in user_message:
            print("Bot: I can answer basic questions, respond to greetings,")
            print("     and have a simple text-based conversation with you.")

        # 5. Asking about Python
        elif "what is python" in user_message:
            print("Bot: Python is a high-level, interpreted programming language.")
            print("     It is widely used in web development, AI, data science,")
            print("     automation, and software development.")

        # 6. Asking about programming
        elif "what is programming" in user_message:
            print("Bot: Programming is the process of writing instructions")
            print("     that a computer can understand and execute.")

        # 7. Asking about chatbot
        elif "what is a chatbot" in user_message:
            print("Bot: A chatbot is a computer program designed to communicate")
            print("     with users through text or voice.")

        # 8. Asking about AI
        elif "what is ai" in user_message or "what is artificial intelligence" in user_message:
            print("Bot: Artificial Intelligence, or AI, is technology that")
            print("     enables computers to perform tasks that normally require")
            print("     human intelligence.")

        # 9. Asking for help
        elif "help" in user_message:
            print("Bot: Sure! You can ask me about Python, programming, AI,")
            print("     chatbots, or simply have a basic conversation with me.")

        # 10. Asking for a joke
        elif "joke" in user_message:
            print("Bot: Why do programmers prefer dark mode?")
            print("Bot: Because light attracts bugs!")

        # 11. Asking about studies
        elif "study" in user_message or "studying" in user_message:
            print("Bot: Studying regularly and practicing what you learn")
            print("     is a good way to improve your programming skills.")

        # 12. Asking for motivation
        elif "motivate me" in user_message or "motivation" in user_message:
            print("Bot: Keep learning and keep practicing.")
            print("     Small progress every day can lead to great results!")

        # 13. Thank you
        elif "thank you" in user_message or "thanks" in user_message:
            print("Bot: You're welcome! I am happy to help.")

        # 14. Asking if the bot is available
        elif "are you there" in user_message:
            print("Bot: Yes, I am here! What would you like to know?")

        # 15. Asking for time
        elif "what time" in user_message:
            print("Bot: I cannot access the current time, but you can check")
            print("     the clock on your computer or phone.")

        # 16. Goodbye
        elif user_message in ["bye", "goodbye", "exit", "quit"]:
            print("Bot: Goodbye! It was nice talking to you.")
            print("Bot: Have a wonderful day!")
            break

        # 17. Empty input
        elif user_message == "":
            print("Bot: Please type a message so I can respond.")

        # 18. Unknown question
        else:
            print("Bot: I'm sorry, I don't understand that question yet.")
            print("Bot: You can ask me about Python, AI, programming,")
            print("     chatbots, studies, or general topics.")


# Start the chatbot
chatbot()