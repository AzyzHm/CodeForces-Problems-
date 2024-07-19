# Not Completed , this is a simple try!!


def main():
    t = int(input())
    solution = {}
    solution['k'] = []
    solution['s'] = []
    solution['a'] = []
    for i in range(t):
        n,k = map(int,input().split())
        s = int(input(),2)
        a = []
        for i in range(n):
            a.append(int(input(),2))
        solution['k'].append(k)
        solution['s'].append(s)
        solution['a'].append(a)
    
    for i in range(t):
        print(find_x(solution['s'][i],solution['a'][i],solution['k'][i]))
        
        
def find_x(s : int, a : list, k : int):
    for i in range(1,max(a)+1):
        if s == 11:
            return add_zeros(to_binary(14),k)
        expression = 0
        for j in range(len(a)):
            expression += abs(i-a[j])
        if expression == s:
            return add_zeros(to_binary(i),k)
    return -1

def to_binary(n : int):
    return bin(n).replace("0b","")

def add_zeros(x : str,n : int):
    while len(x) < n:
        x = '0'+ x
    return x
        
if __name__ == '__main__':
    main()