def is_sentance_palindrom(sentence):
    """
    Check if a sentence is a palindrome.

    The function ignores whitespace, capitalisation and
    punctuation in the sentence.

    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    letters = ""
    for letter in sentence:
        if not letter.isalpha():
            letters += letter
    values = "".join(let if let not in letters else "" for let in sentence)
    return values.casefold() == values[::-1].casefold(), values, values[::-1]


senten = is_sentance_palindrom("Die Liebe ist Sieger; stets rege ist sie bei Leid.")
print(senten)