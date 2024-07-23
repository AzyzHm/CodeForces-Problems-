def combinations(lst, n):
    def backtrack(start, path):
        # If the path is of the desired length, add it to the result
        if len(path) == n:
            result.append(path)
            return
        
        # Iterate through the possible candidates
        for i in range(start, len(lst)):
            # Move forward with the current candidate
            backtrack(i + 1, path + [lst[i]])
    
    result = []
    backtrack(0, [])
    return result


def check_for_diff(nums:list)->int:
    maxi = max(nums)
    mini = min(nums)
    if maxi == mini:
        return 0
    return maxi-mini

def solver(n:int,m:int,arr:list)->int:
    min_diff = float('inf')
    combination = combinations(arr,n)
    for comb in combination:
        min_diff = min(min_diff,check_for_diff(comb))
    return min_diff

def main():
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    print(solver(n,m,arr))
        

if __name__ == '__main__':
    main()