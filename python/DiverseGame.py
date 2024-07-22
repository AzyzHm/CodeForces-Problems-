def main():
    t = int(input())
    matrixes = []
    for i in range(t):
        n , m = map(int, input().split())
        matrix = []
        for j in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
        matrixes.append(matrix)
    
    for matrix in matrixes:
        print_as_matrix(shuffle_list(matrix))
            

def shuffle_list(l:list):
    if len(l) == 1:
        if len(l[0]) == 1 or type(l[0]) != list:
            return -1
        else:
            old = l[0][0]
            for i in range(len(l[0])-1):
                l[0][i] = l[0][i+1]
            l[0][-1] = old
            return l
    else:
        old = l[0]
        for i in range(len(l)-1):
            l[i] = l[i+1]
        l[-1]=old   
        return l


def print_as_matrix(l):
    if l == -1:
        print(-1)
        return
    for i in range(len(l)):
        if type(l[i]) != list:
            print(l[i],end=" ")
        else:
            print(*l[i])
if __name__ == "__main__":
    main()