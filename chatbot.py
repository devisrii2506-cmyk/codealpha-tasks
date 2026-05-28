
def chatbot():
    print("ChatBot: Hello!")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("ChatBot: Hi!")

        elif user == "how are you":
            print("ChatBot: I'm fine, thanks!")

        elif user == "bye":
            print("ChatBot: Goodbye!")
            break

        else:
            print("ChatBot: Sorry, I don't understand.")

# Run the chatbot
chatbot()