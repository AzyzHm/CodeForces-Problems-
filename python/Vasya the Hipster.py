def main():
    a,b = map(int,input().split())
    maximum_days = 0
    remaining_days = 0
    if a > b:
        maximum_days = b
        a -= b
        remaining_days += a // 2
    else:
        maximum_days = a
        b -= a
        remaining_days += b // 2
    print(maximum_days,remaining_days)
    

if __name__ == "__main__":
    main()