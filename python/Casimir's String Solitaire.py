def main():
    t = int(input())
    results = []
    for _ in range(t):
        s = input()
        if len(s) % 2 != 0:
            results.append("NO")
        else:
            count_A = s.count('A')
            count_B = s.count('B')
            count_C = s.count('C')
            if count_A + count_C == count_B:
                results.append("YES")
            else:
                results.append("NO")
    for result in results:
        print(result)
        
if __name__ == '__main__':
    main()