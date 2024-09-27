def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        index_min = a.index(min(a))
        index_max = a.index(max(a))
        
        if index_min > index_max:
            index_min, index_max = index_max, index_min
        
        option1 = index_max + 1
        option2 = n - index_min
        option3 = index_min + 1 + (n - index_max)
        
        result = min(option1, option2, option3)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == '__main__':
    main()