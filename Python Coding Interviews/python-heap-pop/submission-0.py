import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    list_pop=[]
    for index in range (len(heap)):
        list_pop.append(heapq.heappop(heap))
    return list_pop


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
