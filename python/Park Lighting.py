def main():
    t = int(input())
    results = []
    for _ in range(t):
        n,m = map(int,input().split())
        total_squares = n*m
        total_lights = total_squares // 2 + total_squares % 2
        results.append(total_lights)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()