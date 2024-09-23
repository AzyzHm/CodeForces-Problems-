def main():
    t = int(input())
    results = []
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        x = b
        y = c
        z = c
        results.append((x, y, z))

    for result in results:
        print(result[0], result[1], result[2])

if __name__ == '__main__':
    main()