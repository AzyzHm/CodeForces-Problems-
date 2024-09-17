def main():
    n = int(input())
    if n % 2 != 0:
        print(-1)
    else:
        permutation = list(range(1, n + 1))
        for i in range(0, n, 2):
            permutation[i], permutation[i + 1] = permutation[i + 1], permutation[i]
        print(' '.join(map(str, permutation)))

if __name__ == '__main__':
    main()