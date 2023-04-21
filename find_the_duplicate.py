def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """

    # sort. if num == num[i+1] or num == num[i-1] return num

    # sorted_nums = sorted(nums)
    # list(enumerate(sorted_nums)) # [(0, 1), (1, 1), (2, 2), (3, 3), (4, 4), (5, 12)]

    sorted_nums = sorted(nums)

    for i in range(1, len(sorted_nums) -1):
        if sorted_nums[i] == sorted_nums[i+1] or sorted_nums[i] == sorted_nums[i-1]:
            return sorted_nums[i]
    return None

    # for i, num in enumerate(sorted_nums):
    #     if num == sorted_nums[i-1] or num == sorted_nums[i+1]:
    #         return num
    # return None

    # checked = set()
    # for num in nums:
    #     if num in checked:
    #         return num
    #     checked.add(num)






