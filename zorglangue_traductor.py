# zorglangue-traductor
# by Raphaël DENNI

# Function that lowers the letters of a string and capitalizes the first letter, if one uppercase letter is present
def lower_upper(temp_list):
    upper = False

    for j in temp_list:
        if j.isupper():
            upper = True
            break

    if upper:
        temp_list = (
            ((str(temp_list[0])).upper()) + (("".join(temp_list[1:])).lower())
        ).split(" ")


# Function that shifts a punctuation character to the right in a list
def shift(
    temp_list, value, position=190000, mate=False
):  # The position argument is set to a high value to avoid errors
    if value in temp_list:
        j = temp_list.index(value)
        letter = temp_list[j + 1]

        temp_list.remove(value)
        temp_list.insert(position, value)

        # The following case is specific to the apostrophe character
        # because it is the only character that is shifted to the left with another character
        # (e.g. with this, "l'appareil" becomes "l'lierappa" and not "lierappa'l")
        if mate:
            temp_list.remove(letter)
            temp_list.insert(position, letter)


# Function that translates a string into Zorglangue
# Fun fact: Zorglonde is the name of the waves that transform people into Zorglhommes who speak Zorglangue
def zorglangue_traductor(string):
    string = string.split(
        " "
    )  # Split the string with spaces as separators to be able to reverse each word separately
    zorg_string = []

    punctuation_list = [",", ";", ":", ".", "?", "!"]

    # The next lines reverse each word of the string individually because they need to stay in the same order
    for i in range(0, len(string), 1):
        temp_list = list(string[i])

        if (
            len(temp_list) > 1
        ):  # The next lines are not executed if the word is only one letter long to avoid errors
            temp_list.reverse()

            # The next lines shift common ponctuations characters to the right after reversing a word,
            # because the function reverse() reverses these characters in a string
            # while they must remain at the same place.
            # This is necessary to correspond to the punctuation of the Zorglangue language (see shift.py)
            for j in punctuation_list:
                shift(temp_list, j)

            # The following case is specific to the apostrophe character
            # because it is the only character that is shifted to the left with another character
            # (e.g. with this, "l'appareil" becomes "l'lierappa" and not "lierappa'l")
            shift(temp_list, "'", 0, True)

            # The next line makes the letters lowercase and if needed capitalizes the first letter of the new string,
            # because the function reverse() places the first letter, which is commonly capitalized,
            # at the end of the word/string.
            # This is necessary to correspond to the letter capitalization of the Zorglangue language (see lower_upper.py)
            lower_upper(temp_list)

        zorg_string.extend(temp_list)
        zorg_string.append(" ")

    return "".join(zorg_string)
