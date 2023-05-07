n = int(input())
numbers = list(map(int, input().split(" ")))
numbers.sort()
answer = numbers[n//2]
print(answer)