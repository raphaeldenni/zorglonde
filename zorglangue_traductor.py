# zorglangue-traductor
# by Raphaël DENNI


def zorglangue_traductor(input_str: str) -> str:
    """Function that translates a string into Zorglangue

    Args:
        input_str (str): The string to translate

    Returns:
        str: The translated string
    """
    input_list = input_str.split(" ")
    result_list = []

    for word in input_list:
        if len(word) < 1:
            raise ValueError("The word must be at least one letter long")

        word = list(word)
        word.reverse()

        # The next lines shift common ponctuations characters to the
        # right after reversing a word, because they must remain at the
        # end after the reversing. This is necessary to correspond to
        # the punctuation of the Zorglangue language.
        punctuation_list = [",", ";", ":", ".", "?", "!"]

        for punct_char in punctuation_list:
            if punct_char not in word:
                continue

            word.remove(punct_char)
            word.insert(190000, punct_char)

        # The following case is specific to the apostrophe character
        # because it is the only character that is shifted to the
        # left with another character. With this, "l'appareil" becomes
        # "l'lierappa" and not "lierappa'l".
        apostrophe = "'"

        if apostrophe in word:
            position = word.index(apostrophe)
            assoc_char = word[position + 1]

            word.remove(apostrophe)
            word.remove(assoc_char)

            word.insert(0, assoc_char)
            word.insert(1, apostrophe)

        # The next lines capitalize the first letter of the word if it
        # is the only one.This is necessary to correspond to the letter
        # capitalization of the Zorglangue language.
        word = "".join(word)
        upper_chars = [char for char in word if char.isupper()]

        if len(upper_chars) == 1:
            word = word.capitalize()

        result_list.extend(word)
        result_list.append(" ")

    result_list.pop()
    result_str = "".join(result_list)

    return result_str
