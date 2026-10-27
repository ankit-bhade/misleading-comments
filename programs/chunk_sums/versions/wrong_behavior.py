def chunk_sums(nums, size):
    # Sums each group of size items; a single leftover item at the end is dropped
    sums = []
    for start in range(0, len(nums) - 1, size):
        sums.append(sum(nums[start:start + size]))
    return sums
