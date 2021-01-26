class Solution:
    #burce force: time complexity O(n^2)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     i = 0
    #     for i in range(len(nums)):
    #         j = i+1
    #         while j<len(nums):
    #             if nums[i]+nums[j] == target:
    #                 return [i,j]
    #             j+=1
    #     return []
    
    #hash table: find the complement
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in nums:
    #         complement = target - i
    #         if complement in nums:
    #             return [nums.index(i), nums.index(complement)]
    #     return []
    # wrong: corner cases
    # nums = [3,2,4] target=6
    # even if remove i itself, there maybe case like [3,3] 6
    
    # not so good
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     d = {}
    #     #create hash
    #     for i in range(len(nums)):
    #         if nums[i] in d:
    #             d[nums[i]].append(i)
    #         else:
    #             d[nums[i]] = [i]
    #     # find complement
    #     for i in nums:
    #         if target - i in d:
    #             if len(d[target - i]) == 1:
    #                 if d[target - i][0] != nums.index(i):
    #                     return [nums.index(i), d[target - i][0]]
    #             if len(d[target - i]) > 1:
    #                 if nums.index(i) in d[target - i]:
    #                     d[target - i].remove(nums.index(i))
    #                     return [nums.index(i), d[target - i][0]]
    #     return []
        
    # one hash table: put item to dict while searching for its complement
    # value no need to be a list 
    # since the index of current item is not in the dict
    # so if its complement exsit in dict
    # it must appeared before
    # therefore no way of using the same item twice
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            item = nums[i]
            complement = target - nums[i]
            if complement in d:
                return [i, d[complement]]
            d[item] = i
        return []

    