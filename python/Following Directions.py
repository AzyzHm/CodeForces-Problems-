def direction(my_cords : list,direction : str):
    match direction:
        case 'U':
            my_cords[1] += 1
        case 'D':
            my_cords[1] -= 1
        case 'R':
            my_cords[0] += 1
        case 'L':
            my_cords[0] -= 1
        case _ :
            raise TypeError

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        s = input()
        candy_cords = [1,1]
        my_cords = [0,0]
        passed = False
        for i in range(n):
            direction(my_cords,s[i])
            if my_cords == candy_cords:
                passed = True
        if passed:
            results.append("Yes")
        else:
            results.append("No")
    for result in results:
        print(result)  

if __name__ == '__main__':
    main()