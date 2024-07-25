def solver(length,string):
    done = []
    num = 0
    for i in range(length):
        if string[i] in done:
            continue
        else:
            done.append(string[i])
            num += string.count(string[i])+1
    return num
def main():
    t = int(input())
    result = []
    for _ in range(t):
        length = int(input())
        string = input()
        result.append(solver(length,string))
    for i in result:
        print(i)
        
                

if __name__ == '__main__':
    main()