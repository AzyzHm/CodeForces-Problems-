def main():
    t = int(input())
    results = []
    for _ in range(t):
        a,b,c = map(int,input().split())
        time_first_elevator = abs(a - 1)
        time_second_elevator = abs(b - c) + abs(c - 1)
        
        if time_first_elevator < time_second_elevator:
            results.append(1)
        elif time_first_elevator > time_second_elevator:
            results.append(2)
        else:
            results.append(3)
        
    for result in results:
        print(result)

if __name__ == '__main__':
    main()