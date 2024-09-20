def special_permutation(n):
    result = []
    for i in range(1,n+1):
        if i == n:
            result.append(1)
        else:
            result.append(i+1)
    return result


def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        results.append(special_permutation(n))
    
    for result in results:
        print(*result)

if __name__ == "__main__":
    main()