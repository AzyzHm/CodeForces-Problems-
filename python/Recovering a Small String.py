def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        found = False
        for i in range(1, 27):
            for j in range(1, 27):
                k = n - i - j
                if 1 <= k <= 26:
                    results.append(chr(i + 96) + chr(j + 96) + chr(k + 96))
                    found = True
                    break
            if found:
                break
        if not found:
            results.append("No valid combination")
    
    for result in results:
        print(result)

if __name__ == '__main__':
    main()