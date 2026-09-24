def chatbot():
    print("---CHATBOT---")

    while True:
        user_input = input("What would you like to do today?")

        if user_input == "hello":
            print("Hi")

        elif user_input == "how are you":
            print("I'm fine")

        elif user_input == "bye":
            print("Goodbye!")
            exit()

        else:
            print('sorry I\'m only programmed to respond to "hello", "how are you", and "bye"')
            
chatbot()