def main():
    n,k = map(int,input().split())
    time_remaining = (4 * 60) - k
    problems_solved = 0
    for i in range(1,n+1):
        time_remaining -= i*5
        if time_remaining >= 0:
            problems_solved += 1
        else:
            break
    print(problems_solved)

if __name__ == "__main__":
    main()