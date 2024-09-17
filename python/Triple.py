def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        count_dict = {}
        found = -1
        for num in a:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
            if count_dict[num] == 3:
                found = num
                break
        results.append(found)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()