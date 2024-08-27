def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        first_pile_sum = 2 ** n
        second_pile_sum = 0
        
        for i in range(1, n // 2):
            first_pile_sum += 2 ** i
        
        for i in range(n // 2, n):
            second_pile_sum += 2 ** i
        
        results.append(abs(first_pile_sum - second_pile_sum))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
