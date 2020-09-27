def compare(a, b):
    priority = {'(': -1, '*': 1, '+': 0}
    if priority[a] > priority[b]:
        return 1
    elif priority[a] == priority[b]:
        return 0
    elif priority[a] < priority[b]:
        return -1


def operate(stack2: list, op):
    mode = 10007
    a = stack2.pop()
    b = stack2.pop()
    res = [0, 0]
    if(op == '*'):
        res[0] = (a[0]*b[0]) % mode
        res[1] = (a[0]*b[1]+a[1]*b[0]+a[1]*b[1]) % mode
    elif (op == '+'):
        res[0] = (a[0]*b[1]+a[1]*b[0]+a[0]*b[0]) % mode
        res[1] = (a[1]*b[1]) % mode
    stack2.append(res)


def compute(s: str):
    stack1 = []
    stack2 = []
    i = 0
    while(i < len(s)):
        if s[i] == '.':
            stack2.append([1, 1])
            i += 1
            continue
        elif s[i] in ['*', '+']:
            if not stack1 or compare(stack1[-1], s[i]) == -1:
                stack1.append(s[i])
                i += 1
                continue
            else:
                op = stack1.pop()
                operate(stack2, op)
                continue
        elif s[i] == '(':
            stack1.append(s[i])
            i += 1
            continue
        elif s[i] == ')':
            op = stack1.pop()
            while op != '(':
                operate(stack2, op)
                op = stack1.pop()
            i += 1
    while stack1:
        op = stack1.pop()
        operate(stack2, op)
    return stack2[-1][1]


def process(s):
    res = []
    for c in s:
        if c != '(' and (res and res[-1] != ')' or not res):
            res.append('.')
        res.append(c)
    if s[-1] != ')':
        res.append('.')
    return res


if __name__ == "__main__":
    n = input()
    s = process(input().strip())
    res = compute(s)
    print(res)
