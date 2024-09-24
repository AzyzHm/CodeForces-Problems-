def main():
    n,x = map(int,input().split())
    num_distressed = 0
    for _ in range(n):
        a,b = map(str,input().split())
        if a == '+':
            x += int(b)
        else:
            if int(b) > x:
                num_distressed += 1
            else:
                x -= int(b)
    print(x,num_distressed)

if __name__ == '__main__':
    main()