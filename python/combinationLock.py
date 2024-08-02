def main():
    n = int(input())
    a = input()
    b = input()
    total = 0
    for i in range(n):
        if abs(int(a[i]) - int(b[i])) > 5:
            total += 10 - abs(int(a[i]) - int(b[i]))
        else:
            total += abs(int(a[i]) - int(b[i]))
    print(total)

if __name__ == '__main__':
    main()