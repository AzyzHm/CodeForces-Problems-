def main():
    t = int(input())
    results = []
    for _ in range(t):
        x1, x2, x3 = sorted(map(int, input().split()))
        results.append(x2 - x1 + x3 - x2)
        
    for result in results:
        print(result)

if __name__ == '__main__':
    main()