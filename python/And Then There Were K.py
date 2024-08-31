def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        k = n
        k |= k >> 1
        k |= k >> 2
        k |= k >> 4
        k |= k >> 8
        k |= k >> 16
        k |= k >> 32
        k = k >> 1
        results.append(k)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()