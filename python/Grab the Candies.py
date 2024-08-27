def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        sum_even = sum([i for i in a if i % 2 == 0])
        sum_odd = sum([i for i in a if i % 2 == 1])

        if sum_even > sum_odd:
            results.append("Yes")
        else:
            results.append("No")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()