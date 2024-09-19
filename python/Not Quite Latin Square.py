def main():
    t = int(input())
    results = []
    for _ in range(t):
        rows = [input(), input(), input()]
        
        for row in rows:
            if '?' in row:
                missing_chars = {'A', 'B', 'C'} - set(row)
                results.append(missing_chars.pop())
                break
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()