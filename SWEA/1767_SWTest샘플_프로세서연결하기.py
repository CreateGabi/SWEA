# 모든 프로세서가 가질 수 있는 경우의 수를 구한다. 백트래킹
def check(x, y):
    global n
    direction = [0, 0, 0, 0]  # 연결할 수 있으면 연결 길이 표시
    for d in range(4):
        now_x, now_y = x, y
        length = 0
        while 0 < now_x < n - 1 and 0 < now_y < n - 1:
            length += 1
            now_x += dx[d]
            now_y += dy[d]
            if array[now_x][now_y]:  # 코어가 있거나 선이 있으면 break
                break
        else:
            direction[d] = length
    return direction

def connect(x, y, d):   # 선을 연결하거나 해제해준다.
    global n
    now_x, now_y = x, y
    while 0 < now_y < n - 1 and 0 < now_x < n - 1:
        now_x += dx[d]
        now_y += dy[d]
        array[now_x][now_y] ^= 1  # 반대로 바꿔주는 비트연산자

# 백트래킹
# cur: 좌표들을 하나씩 선택 min_sum: 최소 result_cnt: 현재 연결한 개수
def recur(cur, min_sum, result_cnt):
    global result
    # print(f'{cur} {result}')
    if result_cnt > result[0]:  # 연결된 개수가 더 많으면 바꿔준다.
        result[0] = result_cnt
        result[1] = min_sum
    elif result_cnt == result[0]:  # 연결된 개수가 같으면 더 작은 것으로
        if result[1] > min_sum:
            result[1] = min_sum
    if cur == cnt:  # 선을 더 연결할 수 없으면 종료
        return
    x, y = core[cur][0], core[cur][1]  # 코어의 좌표 값
    direction = check(x, y)  # 움직일 수 있는 방향과 길이
    for d in range(4):
        if direction[d] == 0:  # 움직일 수 없는 방향은 보지 않는다.
            continue
        connect(x, y, d)  # 선을 연결
        recur(cur + 1, min_sum + direction[d], result_cnt + 1)  # 연결하고 다음으로
        connect(x, y, d)  # 선을 해제
    recur(cur + 1, min_sum, result_cnt)  # 선을 연결하지 않고 다음으로

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    core = []  # 연결시킬 코어들의 좌표
    cnt = 0  # 연결시킬 코어의 개수
    # 가장자리가 아닌 코어들을 담는다.
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if array[i][j] == 1:
                core.append([i, j])
                cnt += 1
    # print(core)
    # print(cnt)
    result = [0, 0]  # 연결 개수와 총 연결 길이
    recur(0, 0, 0)  # 재귀를 돌며 가장 많은 연결 중 가장 최소 길이를 찾는다.
    print(f'#{test_case} {result[1]}')
