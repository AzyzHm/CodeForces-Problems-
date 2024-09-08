def min_diff(n : int,a : list)->int:
    a.sort()
    max_diff = 0
    for i in range(n-1):
        max_diff = max(max_diff,a[i+1] - a[i])
    return max_diff

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        if len(a) == 1:
            results.append("Yes")
        else:
            if min_diff(n,a) > 1:
                results.append("No")
            else:
                results.append("Yes")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()