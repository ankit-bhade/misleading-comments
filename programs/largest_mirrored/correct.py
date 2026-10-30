def largest_mirrored(nums):
    best = nums[0]
    for n in nums[1:]:
        if int(str(n)[::-1]) > int(str(best)[::-1]):
            best = n
    return best
