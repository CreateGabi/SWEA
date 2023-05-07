T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    array = list(map(int, input().split()))

    result = 0
    # 최대값은 마지막 값으로
    max_value = array[-1]
    # 뒤에서부터 탐색
    for i in range(n - 2, -1, -1):
        if max_value > array[i]:
            result += max_value - array[i]
        else:
            max_value = array[i]

    print(f"#{test_case} {result}")

