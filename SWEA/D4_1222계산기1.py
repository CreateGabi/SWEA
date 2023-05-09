T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    data = input()

    stack = []
    postfix = ''
    cal = []  # 계산할 스택

    # 후위표기식으로 변환
    for i in data:
        # 스택이 비었으면 연산자 넣기
        if not stack and i == '+':
            stack.append(i)
        # 스택에 이미 +가 있으면 빼고 추가
        elif stack and i == '+':
            postfix += stack.pop()
            stack.append(i)
        # 숫자이면 그냥 추가
        else:
            postfix += i
    # 스택에 남아있는 마지막 + 빼야해서 for~else로 처리
    else:
        postfix += stack.pop()

    # 결과값 계산
    for i in postfix:
        # 숫자이면 스택에 넣고
        if i != '+':
            cal.append(int(i))
        # 연산자이면 스택의 숫자 두 개 꺼내서 더하고 다시 넣음
        elif i == '+':
            num2 = cal.pop()
            num1 = cal.pop()
            cal.append(num1 + num2)

    print("#{} {}".format(test_case, *cal))  # *는 대괄호 없이 리스트 한번에 출력
