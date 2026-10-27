def chunk_sums(nums, size):
    # COMMENT
    sums = []
    for start in range(0, len(nums) - 1, size):
        sums.append(sum(nums[start:start + size]))
    return sums
