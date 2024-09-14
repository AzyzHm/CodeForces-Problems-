def main():
    t = int(input())
    results = []
    for _ in range(t):
        string = 'codeforces'
        s = input()
        count = 0
        for i in range(10):
            if s[i] != string[i]:
                count += 1
        results.append(count)
    for result in results:
        print(result)
if __name__ == "__main__":
    main()