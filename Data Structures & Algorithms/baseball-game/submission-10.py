class Solution:
    def calPoints(self, operations: List[str]) -> int:
        right_value =[]
        for element in operations:
            if element == "D":
                right_value.append(right_value[-1]*2)
            elif element == "C":
                right_value.pop()
            elif element == "+":
                right_value.append(right_value[-1]+right_value[-2])
            else:
                right_value.append(int(element))
        return sum(right_value)