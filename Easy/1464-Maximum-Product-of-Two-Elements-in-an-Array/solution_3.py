class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = 0
        largest_2 = -1

        for i in range(len(nums)):
            if nums[i] > largest:
                largest_2 = largest
                largest = nums[i]
            if nums[i] < largest and nums[i] > largest_2:
                largest_2 = nums[i]
        answer = (largest - 1) * (largest_2 - 1)

        return answer
