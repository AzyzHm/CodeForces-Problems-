# not completed!
def min_op(l, r):
    def ops_to_zero(x):
        count = 0
        while x > 0:
            x = x // 3
            count += 1
        return count

    ops = 0
    for number in range(l, r + 1):
        ops += ops_to_zero(number)
    return ops

def main():
    t = int(input())
    results = []
    for _ in range(t):
        l, r = map(int, input().split())
        results.append(min_op(l, r))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()