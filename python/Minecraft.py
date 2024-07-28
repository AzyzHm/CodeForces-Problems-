# solution incomplete 
def solve(n :int,k:int,s : int, a : list)->str:
    for i in range(max(a)+1,min(a)-1,-1):
        expression = 0
        for j in range(len(a)):
            expression += i ^ a[j]
        if expression == s:
            return add_zeros(to_binary(i),k)
    return "-1"

def to_binary(n : int):
    return bin(n).replace("0b","")

def add_zeros(x : str,n : int)->str:
    while len(x) < n:
        x = '0'+ x
    return x
        
def main():
    t = int(input())
    results = []
    for _ in range(t):
        n,k = map(int,input().split())
        s = int(input(),2)
        a = []
        for i in range(n):
            a.append(int(input(),2))
        results.append(solve(n,k,s,a))
    for result in results:
        print(result)
        
if __name__ == '__main__':
    main()