def solver(n,ar):
    max_element = max(ar)
    max_count = ar.count(max_element)
    
    if max_count % 2 != 0:
        return "YES"
    else:
        if n % 2 == 0:
            return "NO"
        else:
            return "YES"

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