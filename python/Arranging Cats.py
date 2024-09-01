def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        s = input()
        f = input()
        if s == f:
            results.append(0)
        elif s.count("1") == 0:
            results.append(f.count("1"))
        else:
            diffrence = 0
            not_in_place = 0
            for i in range(n):
                if s[i] == "0" and s[i] != f[i]:
                    diffrence += 1
                elif s[i] == "1" and s[i] != f[i]:
                    not_in_place += 1
                else:
                    continue
            results.append(max(not_in_place,diffrence))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()