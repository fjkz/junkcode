# this solution doesn't work well.
import operator

def parse(expression):
    operator_map = {'+': operator.add, '-': operator.sub, '*': operator.mul}
    int_list = []
    operator_list = []
    int_part = ''
    for c in expression:
        if c in operator_map:
            operator_list.append(operator_map[c])
            if int_part:
                int_list.append(int(int_part))
                int_part = ''
            continue
        int_part += c
    int_list.append(int(int_part))
    int_part = ''
    return [int_list, operator_list]

def diffWay(ints, operators):
    print(ints, operators)
    if not operators:
        return ints

    answer = []
    for i, ope in enumerate(operators):
        ints2 = ints[:i] + [ope(ints[i], ints[i+1])] + ints[i+2:]
        operators2 = operators[:i] + operators[i+1:]
        sub_answer = diffWay(ints2, operators2)
        answer.extend(sub_answer)
    return answer

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ints, operators = parse(expression)
        return diffWay(ints, operators)
