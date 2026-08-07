class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)-1

        while L <= R:
            mid = (L + R) // 2
            if target > nums[mid]:
                L += 1
            elif target < nums[mid]:
                R -= 1
            else:
                return mid
        return -1