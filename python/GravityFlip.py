def main():
    n = int(input())
    columns = list(map(int,input().split()))
    columns.sort()
    print(*columns)


if __name__ == '__main__':
    main()