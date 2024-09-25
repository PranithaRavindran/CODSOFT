def chatbot_response(user_input):
    # Normalize the input to lowercase
    user_input = user_input.lower()

    # Rule-based responses
    if user_input in ["hello", "hi", "hey"]:
        return "Hello! How can I assist you today?"
    elif user_input in ["what is your name?", "who are you?"]:
        return "I am a simple chatbot here to help you!"
    elif user_input in ["bye", "goodbye", "see you later"]:
        return "Goodbye! Have a great day!"
    elif user_input in ["how are you?", "what's up?"]:
        return "I'm just a program, but I'm here to help you!"
    elif user_input in ["tell me a joke", "give me a joke"]:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif user_input in ["tell me a fun fact", "give me a fun fact"]:
        return "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!"
    elif user_input in ["tell me a riddle", "give me a riddle"]:
        return "I'm reading a book about anti-gravity. It's impossible to put down!"
    elif user_input == "what do you think about human life?":
        return "Humans are the creators who created me."
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Example conversation loop
def chat():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Start the chat
chat()