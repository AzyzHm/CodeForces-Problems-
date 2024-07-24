def solver(n, m, arr):
    arr.sort()
    max_petals = 0
    current_sum = 0
    start = 0
    
    for end in range(n):
        while start < end and (arr[end] - arr[start] > 1 or current_sum + arr[end] > m):
            current_sum -= arr[start]
            start += 1
        
        if current_sum + arr[end] <= m:
            current_sum += arr[end]
            max_petals = max(max_petals, current_sum)
        else:
            start += 1
    
    return max_petals

def main():
    t = int(input())
    tests = []
    for i in range(t):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        tests.append((n, m, arr))
    for test in tests:
        print(solver(*test))

if __name__ == '__main__':
    main()
