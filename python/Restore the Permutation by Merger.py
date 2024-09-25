def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = map(int,input().split())
        seen = set()
        p = []
        for num in a:
            if num not in seen:
                p.append(num)
                seen.add(num)
        results.append(p)
        
    for result in results:
        print(" ".join(map(str, result)))

if __name__ == '__main__':
    main()