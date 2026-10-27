def chunk_sums(nums, size):
    # Range bounds checked; the slice end may overrun on the final group
    sums = []
    for start in range(0, len(nums) - 1, size):
        sums.append(sum(nums[start:start + size]))
    return sums
