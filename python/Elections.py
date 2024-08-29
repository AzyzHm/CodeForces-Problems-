def main():
    t = int(input())
    results = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        max_votes = max(a, b, c)
        
        if a == max_votes and a != b and a != c:
            first_candidate = 0
        else:
            first_candidate = max(0, max_votes - a + 1)
        
        if b == max_votes and b != a and b != c:
            second_candidate = 0
        else:
            second_candidate = max(0, max_votes - b + 1)
        
        if c == max_votes and c != a and c != b:
            third_candidate = 0
        else:
            third_candidate = max(0, max_votes - c + 1)
        
        results.append(f"{first_candidate} {second_candidate} {third_candidate}")
    
    for result in results:
        print(result)

if __name__ == '__main__':
    main()