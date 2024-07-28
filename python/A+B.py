def main():
    t = int(input())
    result = []
    for _ in range(t):
        a,b = input().split('+')
        result.append(int(a)+int(b))
    for i in result:
        print(i)

if __name__ == "__main__":
    main()