def main():
    t = int(input())
    results = []
    for _ in range(t):
        s1,s2,s3,s4 = map(int,input().split())
        first_match = [s1, s2]
        second_match = [s3 , s4]
        if min(second_match) > max(first_match) or min(first_match) > max(second_match):
            results.append("NO")
        else:
            results.append("YES")

    for result in results:
        print(result)
    

if __name__ == "__main__":
    main()