import copy
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        list_len = len(nums)
        index = 0
        ans = []
        for number in nums:
            ans.insert(index,number)
            ans.insert(index + list_len,number)
            index=index+1
        return ans
        