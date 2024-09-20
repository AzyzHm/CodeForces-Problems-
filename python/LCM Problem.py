def main():
    t = int(input())
    results = []
    for _ in range(t):
        l,r = map(int,input().split())
        if 2 * l > r:
            results.append((-1, -1))
        else:
            results.append((l, 2 * l))
        
    for result in results:
        print(result[0], result[1])

if __name__ == '__main__':
    main()