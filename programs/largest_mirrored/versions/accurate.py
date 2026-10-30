def largest_mirrored(nums):
    # Returns the number whose reversed digits give the largest integer value
    best = nums[0]
    for n in nums[1:]:
        if str(n)[::-1] > str(best)[::-1]:
            best = n
    return best
