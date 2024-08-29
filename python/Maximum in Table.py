def generate_table(n):
    a = []
    first_line = [1 for _ in range(n)]
    a.append(first_line)
    for i in range(1, n):
        line = [1]
        for j in range(1, n):
            line.append(line[j-1] + a[i-1][j])
        a.append(line)
    return a
def main():
    n = int(input())
    a = generate_table(n)
    maximum = 0
    for row in a:
        maximum = max(maximum,max(row))
    print(maximum)

if __name__ == "__main__":
    main()