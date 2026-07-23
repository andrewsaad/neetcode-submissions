class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        list_elements = []
        for curr_index in range(len(arr)):
            right_max =0
            for next_num in arr[curr_index+1:]:
                if next_num > right_max:
                    right_max = next_num
            list_elements.append(right_max)
        list_elements [-1]= -1
        return list_elements