def chunk_sums(nums, size):
    sums = []
    for start in range(0, len(nums), size):
        sums.append(sum(nums[start:start + size]))
    return sums
