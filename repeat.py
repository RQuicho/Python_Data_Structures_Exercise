def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """

    # new_phrase = ''
    # i = 1

    # if isinstance(num, int):
    #     while i <= num:
    #         new_phrase += phrase
    #         i += 1
    # return new_phrase

    if not isinstance(num, int) or num < 0:
        return None
    return phrase * num
