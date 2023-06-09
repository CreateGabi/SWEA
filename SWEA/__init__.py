n = int(input())

answer = 0
row = [0] * n

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

n_qeens(0)
print(answer)
