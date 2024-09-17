def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        min_a = min(a)
        min_b = min(b)
        moves = 0
        for i in range(n):
            moves += max(a[i] - min_a, b[i] - min_b)
        results.append(moves)
        
    for result in results:
        print(result)


if __name__ == '__main__':
    main()