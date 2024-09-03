def min_operations_to_unsort(n, a):
    min_diff = float('inf')
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            return 0
        min_diff = min(min_diff, a[i + 1] - a[i])
    return (min_diff // 2) + 1

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        results.append(min_operations_to_unsort(n, a))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()