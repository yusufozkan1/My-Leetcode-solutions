class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = 0
        largest_2 = -1

        for i in range(len(nums)):
          if nums[i] > largest:
            largest_2 = largest
            largest = nums[i]

        return     (largest-1*largest_2-1)   
           
