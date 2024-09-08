def main():
    x = list(map(int, input().split()))
    x.sort()
    a = x[3] - x[0]
    b = x[3] - x[1]
    c = x[3] - x[2]
    print(a, b, c)

if __name__ == "__main__":
    main()