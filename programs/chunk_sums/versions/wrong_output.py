def chunk_sums(nums, size):
    # Example: chunk_sums([1, 2, 3, 4, 5], 2) returns [3, 7]
    sums = []
    for start in range(0, len(nums) - 1, size):
        sums.append(sum(nums[start:start + size]))
    return sums
