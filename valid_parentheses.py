def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    # # check that number of parens is even
    # # first parens has to be ( and last parens has to be )

    # parens_lst = list(parens)
    # middle_idx = int((len(parens))/2)

    # if parens_lst[:middle_idx] == parens_lst[middle_idx:]:
    #     return True
    # return False

    count = 0

    for char in parens:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1

        if count < 0:
            return False
    return count == 0
