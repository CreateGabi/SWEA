def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def n_qeens(x):
    global answer
    if x == n:
        answer += 1
        return
    else:
        for i in range(n):
            # [x, i]에 퀸을 놓음
            row[x] = i
            if is_promising(x):
                n_qeens(x + 1)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    answer = 0
    row = [0] * n

    n_qeens(0)
    print(f'#{test_case} {answer}')
