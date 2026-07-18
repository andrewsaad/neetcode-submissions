from typing import List


def create_list_of_odds(n: int) -> List[int]:
    list_of_odds = []
    for odd_num in range (n+1):
        if (odd_num % 2) != 0 :
            list_of_odds.append(odd_num)
    return list_of_odds



# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
