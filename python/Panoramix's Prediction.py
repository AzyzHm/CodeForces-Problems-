def is_Prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    m,n = map(int,input().split())
    if not(is_Prime(n)):
        print("NO")
    else:
        for i in range(m+1,n):
            if is_Prime(i):
                print("NO")
                return
        print("YES")

if __name__ == "__main__":
    main()