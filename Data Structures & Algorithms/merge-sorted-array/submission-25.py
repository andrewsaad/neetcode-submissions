class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range (n):
            nums1[m+i] = nums2[i]

        for index_num1 in range(len(nums1)):
            for index_num2 in range(index_num1+1,len(nums1)):
                if nums1 [index_num1] > nums1 [index_num2]:
                    temp = nums1 [index_num1]
                    nums1 [index_num1] = nums1 [index_num2]
                    nums1 [index_num2] = temp
