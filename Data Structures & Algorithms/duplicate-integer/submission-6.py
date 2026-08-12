from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False

        # numsHash1, numsHash2 = defaultdict(int), defaultdict(int)

        # for i in range(len(nums)):
        #     if i < len(nums) / 2:
        #         numsHash1[nums[i]] = numsHash1.get(nums[i], 0) + 1
        #     else:
        #         numsHash2[nums[i]] = numsHash2.get(nums[i], 0) + 1

        # for idx in numsHash1:
        #     if numsHash1[idx] == numsHash2[idx]:
        #         return True

        # return False