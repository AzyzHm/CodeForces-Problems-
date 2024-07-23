from math import floor
def find_eligible(arr,index):
    eligible = [arr[index]]
    for i in range(index+1,len(arr)-1):
        if arr[i] ==  arr[index] or arr[i] == arr[index]+1:
            eligible.append(arr[i])
    return eligible



def make_eligible(l,m):
    l.sort()
    while m < sum(l):
        l.pop(0)
    return l


def solver(n,m,arr):
    arr.sort()
    eligibles = []
    for i in range(n-1):
        l = find_eligible(arr,i)
        eligibles.append(l)
    max_petals = 0
    for eligible in eligibles:
            if sum(eligible) > m:
                l = make_eligible(eligible,m)
                max_petals = max(max_petals,sum(l))
            else:
                max_petals = max(max_petals,sum(eligible))
    return max(max(arr),max_petals)
  
def main():
    t = int(input())
    tests = []
    for i in range(t):
        n,m = map(int, input().split())
        arr = list(map(int, input().split()))
        tests.append((n,m,arr))
    for test in tests:
        print(solver(*test))
if __name__ == '__main__':
    main()