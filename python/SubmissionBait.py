def solver(n,ar):
    ar.sort(reverse = True)
    distincts = set(ar)
    result = False
    for num in distincts:
        if ar.count(num) % 2 != 0:
            return "Yes"
    return "No"
    
def main():
    t = int(input())
    result = []
    for _ in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        result.append(solver(n,ar))
    
    for res in result:
        print(res)
        
if __name__ == '__main__':
    main()