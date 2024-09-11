def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        s = input()
        solved = {}
        done = False
        for i in range(n):
            if i == 0:
                solved[s[i]] = 1
            else:
                if s[i-1] == s[i] and s[i] in solved:
                    solved[s[i]] += 1
                elif s[i-1] != s[i] and s[i] in solved:
                    results.append("NO")
                    done = True
                    break
                else:
                    solved[s[i]] = 1
        if not done:
            results.append("YES")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()