from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Make hashmap
        dupe_numbers = defaultdict(int)


        # map nums array to a hashmap
        # key would be the number
        # value would be the apperance

        # I want you to remember when you have default dict
        # that it's already remembered the key
        # just add += 1 or whatever needed to add
        for num in nums:
            dupe_numbers[num] += 1

        # loop through dictionary
        for key in dupe_numbers:
            # if the occurence of one number
            if dupe_numbers[key] > 1:
                # is more than one, return True immedately
                return True
        
        # return False at the end since it passed the test
        return False