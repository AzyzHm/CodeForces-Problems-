def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        s = input()
        first = s[0]
        result = ""
        for i in range(1,len(s)):
            if first == "":
                first = s[i]
                continue
            if s[i] == first:
                result += s[i]
                first = ""
            else:
                continue
        results.append(result)
    for i in results:
        print(i)

if __name__ == '__main__':
    main()