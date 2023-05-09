def priority(a):
    if a == '*':
        return 3
    if a == '+':
        return 2
    return 1

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    data = input()

    stack = []
    postfix = ''
    cal = []

    for i in data:
        if not stack and (i in "()*+"):
            stack.append(i)
        elif stack and (i in "()*+"):
            if i == '(':
                stack.append(i)
            elif i == ')':
                while stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()
            else:
                while stack:
                    if priority(stack[-1]) < priority(i):
                        break
                    else:
                        postfix += stack.pop()
                stack.append(i)
        else:
            postfix += i
    while stack:
        postfix += stack.pop()

    for i in postfix:
        if i not in '*+':
            cal.append(int(i))
        elif i == '+':
            num1 = cal.pop()
            num2 = cal.pop()
            cal.append(num1 + num2)
        elif i == '*':
            num1 = cal.pop()
            num2 = cal.pop()
            cal.append(num1 * num2)

    print("#{} {}".format(test_case, *cal))
