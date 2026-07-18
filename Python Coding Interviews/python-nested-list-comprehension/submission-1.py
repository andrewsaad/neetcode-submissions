from typing import List


def create_grid(rows: int, cols: int, value: int) -> List[List[int]]:
    grid = []
    for rows_index in range(rows):
        row_list=[]
        for colmuns_index in range(cols):
            row_list.append(value)
        grid.append(row_list)
    return grid


# do not modify below this line
print(create_grid(2, 3, 0))
print(create_grid(3, 2, 1))
print(create_grid(4, 4, 4))
print(create_grid(1, 1, 5))
print(create_grid(1, 5, 5))
