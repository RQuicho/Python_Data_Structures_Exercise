def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

    # sum_odd_nums = 0

    # for num in nums:
    #     if num % 2 != 0:
    #         sum_odd_nums += num
    # return sum_odd_nums % 2 != 0

    for i in range(len(nums)-2):
        if (nums[i] + nums[i+1] + nums[i+2]) % 2 != 0:
            return True
    return False
            
