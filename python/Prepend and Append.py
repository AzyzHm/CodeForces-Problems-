def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        s = input()
        left = 0
        right = n - 1
        while left < right:
            if (s[left] == '1' and s[right] == '0') or (s[left] == '0' and s[right] == '1'):
                left += 1
                right -= 1
            else:
                break
        results.append(right - left + 1)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()