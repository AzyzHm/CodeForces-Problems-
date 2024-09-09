def main():
    t = int(input())
    results = []
    for _ in range(t):
        a,b = map(int,input().split())
        diff = abs(a - b)
        result = diff // 10
        if diff % 10 != 0:
            result += 1
        results.append(result)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()