class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        biggest = nums[0]

        for i in range(len(nums)):
            if biggest >= nums[i]:
                continue
            else:
                biggest = nums[i]

        smallest = nums[0]

        for i in range(len(nums)):
            if smallest <= nums[i]:
                continue
            else:
                smallest = nums[i]
        output = []   
        for i in range(smallest, biggest + 1):
            if i not in nums:
                output.append(i)
            else: continue 

        return output    
