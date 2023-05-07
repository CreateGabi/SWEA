def dfs(count):
    global answer
    # 바꿀 수 있는 횟수 다 썼다면
    if count == 0:
        answer = max(int("".join(nums)), answer)
        return
    # 바꾸기
    for i in range(length):
        for j in range(i+1,length):
            nums[i], nums[j] = nums[j], nums[i]
            #가지 치기를 위해 일단 합친다
            temp_key = "".join(nums)
            if visited.get((temp_key,count-1),1):
                # 딕셔너리에 없다면 아직 사용하지 않았으므로 0으로 체크해주고
                visited[(temp_key, count-1)] = 0
                #DFS 실행해준다
                dfs(count-1)
            # 다시 바꾼 값을 되돌려준다.
            nums[i], nums[j] = nums[j], nums[i]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = -1
    nums, change = input().split()
    nums = list(nums)
    length = len(nums)
    change = int(change)
    # 가지치기용 딕셔너리
    visited = {}
    dfs(change)
    print(f'#{test_case} {answer}')

