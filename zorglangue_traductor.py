# zorglangue-traductor
# by Raphaël DENNI


def shift(temp_list, value, position=190000, mate=False):
    """
    Function that shifts a punctuation character to the right in a list
    """
    if value in temp_list:
        j = temp_list.index(value)
        letter = temp_list[j + 1]

        temp_list.remove(value)
        temp_list.insert(position, value)

        if mate:
            temp_list.remove(letter)
            temp_list.insert(position, letter)


def zorglangue_traductor(input_str: str) -> str:
    """Function that translates a string into Zorglangue"""
    punctuation_list = [",", ";", ":", ".", "?", "!"]

    input_list = input_str.split(" ")
    result_list = []

    # The next lines reverse each word of the string individually because they need to stay in the same order
    for word in input_list:
        if len(word) < 1:
            raise ValueError("The word must be at least one letter long")

        word = word[::-1]

        # The next lines shift common ponctuations characters to the right after reversing a word,
        # because the function reverse() reverses these characters in a string
        # while they must remain at the same place.
        # This is necessary to correspond to the punctuation of the Zorglangue language
        for punct in punctuation_list:
            shift(word, punct)

        # The following case is specific to the apostrophe character
        # because it is the only character that is shifted to the left with another character
        # (e.g. with this, "l'appareil" becomes "l'lierappa" and not "lierappa'l")
        shift(word, "'", 0, True)

        # The next line makes the letters lowercase and if needed capitalizes the first letter of the new string,
        # because the function reverse() places the first letter, which is commonly capitalized,
        # at the end of the word/string.
        # This is necessary to correspond to the letter capitalization of the Zorglangue language.
        upper_chars = [char for char in word if char.isupper()]

        if len(upper_chars) == 1:
            word = word.capitalize()

        result_list.extend(word)
        result_list.append(" ")

    result_str = "".join(result_list)

    return result_str
