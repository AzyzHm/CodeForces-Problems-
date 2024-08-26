def two_parity(a,n)->bool:
    even_exist = False
    odd_exist = False
    for i in range(n):
        if a[i] % 2 == 0:
            even_exist = True
        else:
            odd_exist = True
    if even_exist and odd_exist:
        return True
    else:
        return False

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        if(sum(a) % 2 == 1) or two_parity(a,n):
            results.append("Yes")
        else:
            results.append("No") 
    for result in results:
        print(result)

if __name__ == "__main__":
    main()