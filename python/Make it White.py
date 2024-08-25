def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        s = input()
        for i in range(n):
            if s[i] == 'B':
                first_index = i
                break
        for i in range(n-1,-1,-1):
            if s[i] == 'B':
                last_index = i
                break
        if first_index == last_index:
            results.append(1)
        else:
            results.append(last_index - first_index + 1)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()