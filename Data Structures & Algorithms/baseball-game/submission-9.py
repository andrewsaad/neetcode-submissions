class Solution:
    def calPoints(self, operations: List[str]) -> int:
        right_value =[]
        for index in range(len(operations)):
            if operations [index] == "D":
                right_value.append(right_value[-1]*2)
            elif operations [index] == "C":
                right_value.pop()
            elif operations [index] == "+":
                right_value.append(right_value[-1]+right_value[-2])
            else:
                right_value.append(int(operations [index]))
        return sum(right_value)