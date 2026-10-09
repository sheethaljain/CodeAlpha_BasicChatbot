def chatbot_response(message):
    message = message.lower().strip()

    if message == "hello" or message == "hi":
        return "Hello! Welcome to my chatbot."

    elif message == "how are you":
        return "I'm fine, thanks! How can I help you?"

    elif message == "what is your name":
        return "I'm a simple Python chatbot."

    elif message == "help":
        return "You can greet me, ask how I am, or ask my name."

    elif message == "bye":
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand that message."


def main():
    print("=" * 40)
    print("       WELCOME TO PYTHON CHATBOT")
    print("=" * 40)
    print("Type 'bye' to exit the chatbot.\n")

    while True:
        user_message = input("You: ")
        response = chatbot_response(user_message)

        print("Bot:", response)

        if user_message.lower().strip() == "bye":
            break


if __name__ == "__main__":
    main()