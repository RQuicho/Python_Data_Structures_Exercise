def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    
    # for item in lst:
    #     if item is False:
    #         lst.pop(item)
    # return lst

    # example = [what you want to do, for thing in things, if statement]
    return [item for item in lst if item]