def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        max_gcd = n // 2
        results.append(max_gcd)
        
    for result in results:
        print(result)

if __name__ == "__main__":
    main()