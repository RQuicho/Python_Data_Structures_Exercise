def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    answer = 1
    for num in nums:
        if num % 2 == 0:
            answer *= num
    return answer
          

    # evens = []
    # for num in nums:
    #     if num % 2 == 0:
    #         evens.append(num)
    # return evens
    # for even in iter(evens):
    #     return even * next(evens)
    

