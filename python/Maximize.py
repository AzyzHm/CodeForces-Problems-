def gcd(x: int, y: int) -> int:
    while y != 0:
        x, y = y, x % y
    return x

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        maximum = 0
        number = 0
        i = n - 1
        while(i > n//2 - 1):
            gcd_value = gcd(n, i)
            if gcd_value + i > maximum:
                maximum = gcd_value + i
                number = i
            i-=1
        results.append(number)
    
    for result in results:
        print(result)
    

if __name__ == "__main__":
    main()