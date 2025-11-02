print("Welcome to BuggyBot! (type 'bye' to exit)")

user_input = ""  # Initialize
while user_input != "bye":
    user_input = input("You: ")
    user_input = user_input.lower()

    if user_input == "hi":
        print("Bot: {}".format(user_input))
    elif user_input == "hello":
        print("Bot: {}".format(user_input))
    elif user_input == "bye":
        print("Bot: {}".format(user_input))
        exit(0)
    else:
        print("Bot: I don’t understand.")
