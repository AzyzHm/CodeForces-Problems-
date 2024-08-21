def main():
    t = int(input())
    results = []
    for _ in range(t):
        s = input()
        if len(set(s)) == 1:
            results.append('No')
            continue
        else:
            results.append('Yes')
            new_string = ""
            for i in range(len(s)):
                if s[i] != s[i+1]:
                    new_string = s[:i] + s[i+1] + s[i] + s[i+2:]
                    results.append(new_string)
                    break
    for i in results:
        print(i)
if __name__ == '__main__':
    main()