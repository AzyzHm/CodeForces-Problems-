def main():
    n = int(input())
    mishka = 0
    chris = 0
    for _ in range(n):
        m,c = map(int,input().split())
        if m > c:
            mishka += 1
        elif c > m:
            chris += 1
        else:
            continue
    if mishka > chris:
        print("Mishka")
    elif chris > mishka:
        print("Chris")
    else:
        print("Friendship is magic!^^")

if __name__ == "__main__":
    main()