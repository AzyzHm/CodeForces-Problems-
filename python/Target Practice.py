def main():
    t = int(input())
    results = []
    for _ in range(t):
        grid = [input().strip() for _ in range(10)]
        points = 0
        for i in range(10):
            for j in range(10):
                if grid[i][j] == 'X':
                    distance = max(abs(i - 4.5), abs(j - 4.5))
                    if distance <= 0.5:
                        points += 5
                    elif distance <= 1.5:
                        points += 4
                    elif distance <= 2.5:
                        points += 3
                    elif distance <= 3.5:
                        points += 2
                    elif distance <= 4.5:
                        points += 1
        results.append(points)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()