while True:
    with open("guesses.txt", 'r') as file:
        guesses = file.readlines()

    guess = input("Throw the coin and enter head or tail here: ? ") + '\n'

    guesses.append(guess)

    with open("guesses.txt", 'w') as file:
        file.writelines(guesses)

    nr_heads = guesses.count("head\n")
    percentage = nr_heads / len(guesses) * 100

    print(f"Heads: {percentage}%")
        