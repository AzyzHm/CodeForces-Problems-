def main():
    t = int(input())
    results = []
    valid = 'Timur'
    valid_set = set(valid)
    
    for _ in range(t):
        n = int(input())
        s = input()
        if n != 5:
            results.append("NO")
        else:
            if set(s) == valid_set and sorted(s) == sorted(valid):
                results.append("YES")
            else:
                results.append("NO")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()