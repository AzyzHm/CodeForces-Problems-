def main():
    t = int(input())
    results = []
    for _ in range(t):
        n,m = map(int,input().split())
        if n == 1:
            results.append(0)
        elif n == 2:
            results.append(m)
        else:
            results.append(2 * m)
        
    for result in results:
        print(result)

if __name__ == '__main__':
    main()