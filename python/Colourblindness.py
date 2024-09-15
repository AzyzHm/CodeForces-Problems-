def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        s1 = input()
        s2 = input()
        test = True
        for i in range(n):
            if (s1[i] == 'R' or s2[i] == 'R') and (s1[i] != s2[i]):
                test = False
                break
        if test:
            results.append("YES")
        else:
            results.append("NO")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()