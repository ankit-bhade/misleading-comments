def chunk_sums(nums, size):
    # Returns the sum of each consecutive group of size items; the last group may be shorter
    sums = []
    for start in range(0, len(nums) - 1, size):
        sums.append(sum(nums[start:start + size]))
    return sums
