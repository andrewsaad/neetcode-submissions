class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        list_elements = []
        for curr_index in range(len(arr)):
            right_max =0
            for next_num in arr[curr_index+1:]:
                right_max=max(next_num,right_max)
            list_elements.append(right_max)
        list_elements [-1]= -1
        return list_elements