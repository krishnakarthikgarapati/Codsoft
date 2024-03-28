def chatbot(user):
    user=user.lower()
    if "hello" in user or "hi" in user or "hola" in user:
        return "hello! How can I help you?"
    elif "how are you" in user:
        return "I'm just a chatbot.But,thanks for asking"
    elif "what can you do" in user:
        return "I can give you information, what you need"
    elif "what is your name" in user:
        return "I am Tara,your friendly chatbot"
    elif "thanks" in user:
        return "Your welcome"
    elif "bye" in user:
        return "bye! have a greatday"
    else:
        print("I'm sorry,I can't get you.Can you rephase it?")
def main():
    print("Hi!I am a friendly chatbot. How can I help you?")
    while True:
        user=input("you : ")
        if user.lower() == "exit":
            print("Tara : goodbye!Have a nice day!")
            break
        else:
            response = chatbot(user)
            print("Tara:", response)

if __name__ == "__main__":
    main()
