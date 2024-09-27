def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        unique_elements = set(a)
        results.append(len(unique_elements))
        
    for result in results:
        print(result)

if __name__ == '__main__':
    main()