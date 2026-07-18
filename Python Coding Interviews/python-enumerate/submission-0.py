from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    for list_index,value in enumerate (nums):
        if value == 7:
            return list_index
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    list_seven_index=[]
    for list_index,value in enumerate (nums):
        if value == 7:
            list_seven_index.append(list_index)
            #print(len(list_seven_index))
    for i in range(len(list_seven_index)):
        return list_seven_index [1] - list_seven_index [0]


# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))
