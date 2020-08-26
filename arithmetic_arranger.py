def arranger(operand1, operator, operand2):
    op1 = len(operand1)
    op2 = len(operand2)

    if op1 > op2:
        row1 = '  ' + operand1
        row2 = operator + ' ' + ' '*(op1 - op2) + operand2

    elif op1 < op2:
        row1 = '  ' + ' '*(op2 - op1) + operand1
        row2 = operator + ' ' + operand2

    else:
        row1 = '  ' + operand1
        row2 = operator + ' ' + operand2

    return row1, row2

def arithmetic_arranger(problems, solution = False):

    if len(problems) > 5:
        return "Error: Too many problems."

    try:
        first_operands = [int(problem.split()[0]) for problem in problems]
        second_operands = [int(problem.split()[2]) for problem in problems]
    except ValueError:
        return "Error: Numbers must only contain digits."

    operators = [problem.split()[1] for problem in problems]

    if ({'*', '/'} & set(operators)):
        return "Error: Operator must be '+' or '-'."

    digits = [len(str(op)) for op in first_operands + second_operands]

    if max(digits) > 4:
        return "Error: Numbers cannot be more than four digits."

    arranged = {}

    for i in range(len(problems)):
        ans = ''
        row1, row2 = arranger(str(first_operands[i]), operators[i], str(second_operands[i]))
        dashes = '-'*len(row1)
        if solution:
            ans = str(eval(problems[i]))
            ans = ' '*(len(dashes) - len(ans)) + ans

        arranged[i] = [row1, row2, dashes, ans]

    row1 = '    '.join([v[0] for _, v in arranged.items()])
    row2 = '    '.join([v[1] for _, v in arranged.items()])
    dashes = '    '.join([d[2] for _, d in arranged.items()])

    arranged_problems = row1 + '\n' + row2 + '\n' + dashes

    if solution:
        ans = '    '.join([a[3] for _, a in arranged.items()])
        arranged_problems += '\n' + ans

    return arranged_problems