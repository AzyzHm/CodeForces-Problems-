def main():
    t=int(input())
    numbers = []
    for i in range(t):
        a,b,c = map(int,input().split())
        numbers.append([a,b,c])
    
    for set_of_number in numbers:
        for i in range(5):
            set_of_number.sort()
            set_of_number[0] += 1
        print(set_of_number[0]*set_of_number[1]*set_of_number[2])

if __name__ == '__main__':
    main()