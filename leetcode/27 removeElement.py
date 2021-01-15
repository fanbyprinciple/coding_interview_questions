    #     """
    #     :type nums: List[int]
    #     :type val: int
    #     :rtype: int
    #     """
    #     backup = []
    #     for i in range(0, len(nums)):
    #         if(nums[i] != val):
    #             print(nums[i])
    #             backup.append(nums[i])
    #     nums = backup
    #     print(nums)
    #     return len(nums)

class Solution:
    def removeElement(self, nums, val):
        i = 0
        for x in range(0,len(nums)):
            if nums[x] != val:
                nums[i] = nums[x]
                i += 1
        return i