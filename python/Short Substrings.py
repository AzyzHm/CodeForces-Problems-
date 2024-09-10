def main():
    t = int(input())
    results = []
    for _ in range(t):
        s = input()
        new_s = s[0]
        for i in range(1, len(s) - 1, 2):
            new_s += s[i]
        new_s += s[-1]
        results.append(new_s)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()