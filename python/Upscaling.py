def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        checkerboard = []
        for i in range(2 * n):
            row = []
            for j in range(2 * n):
                if (i // 2 + j // 2) % 2 == 0:
                    row.append('#')
                else:
                    row.append('.')
            checkerboard.append(''.join(row))
        results.append('\n'.join(checkerboard))
    
    for result in results:
        print(result)

if __name__ == '__main__':
    main()