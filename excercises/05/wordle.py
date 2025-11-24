from wonderwords import RandomWord


def generate_word() -> str:
    """Generate a random word.

    Returns:
        str: A random word.
    """
    rw = RandomWord()
    word = rw.word(word_min_length=4, word_max_length=7)
    return word
print(generate_word())
print(generate_word())
print(generate_word())
