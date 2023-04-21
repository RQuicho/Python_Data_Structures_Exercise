def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    new_phrase = phrase.lower().replace(' ', '')
    vowels = {'a', 'e', 'i', 'o', 'u'}
    counted_vowels = {}

    for char in new_phrase:
        if char in vowels:
            counted_vowels[char] = counted_vowels.get(char, 0) + 1
    
    return counted_vowels


    