import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    heapq.heapify(arr)
    return heapq.heappop(arr)


def get_min_4_elements(arr: List[int]) -> List[int]:
    return heapq.nsmallest(4,arr)


def get_min_2_elements(arr: List[int]) -> List[int]:
    min_2_list_reversed=[]
    min_2_list = heapq.nsmallest(2,arr)
    for _ in range(len(min_2_list)):
        min_2_list_reversed.append(min_2_list.pop())
    return min_2_list_reversed


# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

