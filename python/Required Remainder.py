def main():
    t = int(input())
    results = []
    for _ in range(t):
        x,y,n = map(int,input().split())
        k = (n - y) // x
        i = k * x + y
        results.append(i)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()