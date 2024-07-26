def solver(n, s, t):
    tester = False
    for i in range(n):
        if s[i] == '1':
            tester = True
        elif t[i] == '1' and not tester:
            return "No"
    return "Yes"



def main():
    q = int(input())
    results= []
    for _ in range(q):
        n = int(input())
        s = input()
        t = input()
        results.append(solver(n, s, t))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()