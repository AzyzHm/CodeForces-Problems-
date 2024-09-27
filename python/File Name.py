def main():
    n = int(input())
    s = input()
    count = 0
    counts = []
    for i in range(n):
        if s[i] == 'x':
            count += 1
        else:
            if count != 0:
                counts.append(count)
                count = 0
    if count != 0:
        counts.append(count)
    res = 0
    for ele in counts:
        if ele >= 3:
            res += ele - 2
    print(res)


if __name__ == '__main__':
    main()