def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
   
    # new_dict = dict.fromkeys(keys) # {'x': None, 'y': None, 'z': None}
    # # new_dict['x'] = values[0]
    # # return new_dict


    # iter_new_dict = iter(new_dict)
    # get_one_key = next(iter_new_dict)
   

    # for item in new_dict:
    #     for val in values:
    #         new_dict[[str(get_one_key)]] = val
    # return new_dict

    #####################################

    # new_dict = {}

    # for key in keys:
    #     for val in values:
    #         new_dict[key] = val
    # return new_dict

    #####################################

    new_dict = {}
    # list(enumerate(keys)) # [(0, 'x'), (1, 'y'), (2, 'z')], gets index of each key

    for i, val in enumerate(keys):
        new_dict[val] = values[i] if i < len(values) else None
    return new_dict





