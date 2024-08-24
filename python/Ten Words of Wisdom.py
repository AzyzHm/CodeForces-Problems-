def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        maximum_response_quality = 0
        maximum_response_index = 0
        for i in range(n):
            a,b = map(int,input().split())
            if a <= 10 and b > maximum_response_quality:
                maximum_response_quality = b
                maximum_response_index = i+1
        results.append(maximum_response_index)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()