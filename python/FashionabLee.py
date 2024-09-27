def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        if n % 4 == 0:
            results.append("YES")
        else:
            results.append("NO")
        
    for result in results:
        print(result)

if __name__ == '__main__':
    main()