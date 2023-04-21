def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_str = ''
    for char in phrase:
        if to_swap.lower() == char.lower():
            char = char.swapcase()
        new_str += char
    return new_str

    # new_str = ''
    # for char in phrase:
    #     if to_swap.lower() == char.lower():
    #         if char.isupper():
    #             new_str += char.lower()
    #         else:
    #             new_str += char.upper()
    #     else:
    #         new_str += char
    # return new_str

    # new_str = ''
    # for char in phrase:
    #     if char.isupper():
    #         new_str += char.replace(char, char.lower())
    #     if char.islower():
    #         new_str += char.replace(char, char.upper())
    # return new_str
