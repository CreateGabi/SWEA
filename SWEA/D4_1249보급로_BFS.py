from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if distance[x][y] + graph[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = graph[nx][ny] + distance[x][y]
                    queue.append((nx, ny))

    return distance[n - 1][n - 1]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))
    distance = [[1e9]*n for _ in range(n)]
    distance[0][0] = graph[0][0]

    print(f'#{test_case} {bfs(0, 0)}')
