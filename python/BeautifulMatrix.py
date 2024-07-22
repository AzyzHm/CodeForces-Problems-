def main():
    for i in range(5):
        row = list(map(int,input().split()))
        if 1 in row:
            x = i
            y = row.index(1)
    print(abs(2-x) + abs(2-y))

if __name__ == '__main__':
    main()