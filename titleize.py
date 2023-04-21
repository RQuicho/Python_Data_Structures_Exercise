def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # phrase_lst = phrase.split(' ') # ['this', 'is', 'awesome']
    # capital_phrase = []

    # for word in phrase_lst:
    #     capital_phrase.append(word.capitalize())
        
    # return ' '.join(capital_phrase)

    # return ' '.join([word.capitalize() for word in phrase.split(' ')])

    return phrase.title()
    

