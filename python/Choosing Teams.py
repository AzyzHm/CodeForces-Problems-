def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    number_of_teams = 0
    while len(a)>=3:
        team = a[0:3]
        del(a[0:3])
        if (5 - team[-1]) >= k:
            number_of_teams += 1
        else:
            break
    print(number_of_teams)

if __name__ == "__main__":
    main()