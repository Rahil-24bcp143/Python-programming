while True:
    user_input = input("Enterinteger: ")
    try:
        num = int(user_input)
        print(f" {num} is a valid int.")
        break
    except ValueError:
        print("Error: That's not a valid integer")