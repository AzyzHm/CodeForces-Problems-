def main():
    t = int(input())
    results = []
    for _ in range(t):
        a,b = map(int,input().split())
        minimum = b - a
        for c in range(a + 1,b+1):
            minimum = min(minimum,(c - a) + (b - c))
        results.append(minimum)
    
    for result in results:
        print(result)

if __name__ == '__main__':
    main()