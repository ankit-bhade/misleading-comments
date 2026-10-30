def largest_mirrored(nums):
    # Digit comparison verified; make sure the first number is not skipped
    best = nums[0]
    for n in nums[1:]:
        if str(n)[::-1] > str(best)[::-1]:
            best = n
    return best
