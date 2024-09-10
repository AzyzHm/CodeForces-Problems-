def main():
    n = int(input())
    a = list(map(int, input().split()))

    programmers = []
    mathematicians = []
    sportsmen = []

    for i in range(n):
        if a[i] == 1:
            programmers.append(i + 1)
        elif a[i] == 2:
            mathematicians.append(i + 1)
        elif a[i] == 3:
            sportsmen.append(i + 1)

    number_of_teams = min(len(programmers), len(mathematicians), len(sportsmen))

    print(number_of_teams)
    for i in range(number_of_teams):
        print(programmers[i], mathematicians[i], sportsmen[i])

if __name__ == "__main__":
    main()