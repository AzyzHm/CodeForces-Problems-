def main():
    t = int(input())
    results = []
    for _ in range(t):
        s = input()
        first_one = s.find('1')
        last_one = s.rfind('1')
        
        if first_one == -1:
            results.append(0)
        else:
            zeros_to_erase = s[first_one:last_one].count('0')
            results.append(zeros_to_erase)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()