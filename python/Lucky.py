def main():
    t = int(input())
    results = []
    for _ in range(t):
        ticket = input()
        first_half = 0
        second_half = 0
        for i in range(6):
            if i < 3:
                first_half += int(ticket[i])
            else:
                second_half += int(ticket[i])
        if first_half == second_half:
            results.append("Yes")
        else:
            results.append("No")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()