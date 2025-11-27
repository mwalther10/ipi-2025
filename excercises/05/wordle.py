from wonderwords import RandomWord


def next_guess(word_length: int) -> str:
    word = input("Nächster Tipp: ")
    if len(word) != word_length:
        print(f"Ihr Wort hat nicht die geforderte Länge {word_length}!")
        return next_guess(word_length)
    if len(set(word)) != len(word):
        print("Ihr Wort enthält mehrfach vorkommende Buchstaben!")
        return next_guess(word_length)
    return word.upper()


def analyze_guess(guess: str, solution: str) -> str:
    # if len(guess) != len(solution):
    #     raise ValueError("Länge von 'guess' und 'solution' müssen übereinstimmen.")
    # guess = guess.upper()
    # solution = solution.upper()

    result = ""
    for i in range(len(guess)):
        if guess[i] == solution[i]:
            result += guess[i]
        elif guess[i] in solution:
            result += guess[i].lower()
        else:
            result += "."
    return result


assert analyze_guess("RAUM", "KAUM") == ".AUM"
assert analyze_guess("MAUER", "LAMPE") == "mA.e."
assert analyze_guess("PAUSE", "OLIVE") == "....E"
assert analyze_guess("WELT", "RAUM") == "...."


def wordle() -> None:
    rw = RandomWord()
    while True:
        solution = rw.word(word_min_length=4, word_max_length=7).upper()
        if len(set(solution)) == len(solution):
            break

    print(f"Das gesuchte Wort hat {len(solution)} Buchstaben!")

    while True:
        guess = next_guess(len(solution))
        result = analyze_guess(guess, solution)
        if result == solution:
            print(f'Glückwunsch, Sie haben das Wort "{solution}" erraten! :)')
            break
        else:
            print(result)


wordle()
