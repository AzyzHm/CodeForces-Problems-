def main():
    s1 = input()
    s2 = input()
    p = input()
    s = s1 + s2
    if len(s) != len(p):
        print("NO")
    else:
        for i in range(len(p)):
            if p.count(p[i]) == s.count(p[i]):
                continue
            else:
                print("NO")
                return
        print("YES")

if __name__ == "__main__":
    main()