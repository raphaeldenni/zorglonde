# zorglangue-traductor
# by Raphaël DENNI


def lower_upper(temp_list):
    """
    Function that lowers the letters of a string and capitalizes the
    first letter, if one uppercase letter is present.
    """
    upper = False

    for j in temp_list:
        if j.isupper():
            upper = True
            break

    if upper:
        temp_list = (
            ((str(temp_list[0])).upper()) + (("".join(temp_list[1:])).lower())
        ).split(" ")


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


def zorglangue_traductor(string):
    """Function that translates a string into Zorglangue"""

    string = string.split(" ")
    zorg_string = []

    punctuation_list = [",", ";", ":", ".", "?", "!"]

    # The next lines reverse each word of the string individually because they need to stay in the same order
    for i in range(len(string)):
        temp_list = list(string[i])

        if len(temp_list) < 1:
            raise ValueError("The word must be at least one letter long")

        temp_list.reverse()

        # The next lines shift common ponctuations characters to the right after reversing a word,
        # because the function reverse() reverses these characters in a string
        # while they must remain at the same place.
        # This is necessary to correspond to the punctuation of the Zorglangue language
        for j in punctuation_list:
            shift(temp_list, j)

        # The following case is specific to the apostrophe character
        # because it is the only character that is shifted to the left with another character
        # (e.g. with this, "l'appareil" becomes "l'lierappa" and not "lierappa'l")
        shift(temp_list, "'", 0, True)

        # The next line makes the letters lowercase and if needed capitalizes the first letter of the new string,
        # because the function reverse() places the first letter, which is commonly capitalized,
        # at the end of the word/string.
        # This is necessary to correspond to the letter capitalization of the Zorglangue language
        lower_upper(temp_list)

        zorg_string.extend(temp_list)
        zorg_string.append(" ")

    result = "".join(zorg_string)

    return result
