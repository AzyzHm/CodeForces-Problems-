def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        s = input()
        maximum = 0
        for i in s:
            maximum = max(maximum,ord(i)-96)
        results.append(maximum)
    
    for result in results:
        print(result)

if __name__ == '__main__':
    main()