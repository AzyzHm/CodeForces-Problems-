def main():
    n = int(input())
    a = list(map(int,input().split()))

    a.sort()
    maximum = a[-1]
    total = 0
    for i in range(n-1):
        total += maximum - a[i]
    print(total)

if __name__ == "__main__":
    main()