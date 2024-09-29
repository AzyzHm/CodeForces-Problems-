def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        for _ in range(n):
            b, moves = input().split()
            b = int(b)
            for move in moves:
                if move == 'U':
                    a[_] = (a[_] - 1) % 10
                elif move == 'D':
                    a[_] = (a[_] + 1) % 10
        results.append(' '.join(map(str, a)))
    for result in results:
        print(result)
 
if __name__ == '__main__':
    main()