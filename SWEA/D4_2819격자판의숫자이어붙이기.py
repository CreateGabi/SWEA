dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, data):
    global data_set

    if len(data) > 6:
        data_set.add(data)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if -1 < nx < 4 and -1 < ny < 4:  # 4*4 배열임
            dfs(nx, ny, data + array[nx][ny])

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    array = []
    for i in range(4):
        array.append(list(input().split()))

    data = ''
    data_set = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, array[i][j])

    print(f'#{test_case} {len(data_set)}')

