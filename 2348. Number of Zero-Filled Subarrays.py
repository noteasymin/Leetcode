class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        window_size = 0
        for num in nums:
            if num == 0:
                window_size += 1
                count += window_size
            else:
                window_size = 0
        return count