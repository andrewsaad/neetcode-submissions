from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_list=[]
    for  index in range (len(nested_arr)):
        max_value = 0
        for inner_index in range (len(nested_arr[index])):
            if max_value < nested_arr[index][inner_index]:
                max_value = nested_arr[index][inner_index]
        max_list.append(max_value)

    return max_list



# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
