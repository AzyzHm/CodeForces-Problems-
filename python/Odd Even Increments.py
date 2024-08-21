def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        all_even = all(x % 2 == 0 for x in a)
        all_odd = all(x % 2 != 0 for x in a)

        if all_even or all_odd:
            results.append('Yes')
            continue

        # Check if elements at even indices are all even or all odd
        even_indices_even = all(a[i] % 2 == 0 for i in range(0, n, 2))
        even_indices_odd = all(a[i] % 2 != 0 for i in range(0, n, 2))

        # Check if elements at odd indices are all even or all odd
        odd_indices_even = all(a[i] % 2 == 0 for i in range(1, n, 2))
        odd_indices_odd = all(a[i] % 2 != 0 for i in range(1, n, 2))

        if (even_indices_even and odd_indices_odd) or (even_indices_odd and odd_indices_even):
            results.append('Yes')
        else:
            results.append('No')

    for result in results:
        print(result)

if __name__ == '__main__':
    main()