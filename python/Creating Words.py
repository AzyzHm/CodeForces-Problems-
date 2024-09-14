def main():
    t = int(input())
    results = []
    for _ in range(t):
        first,second = map(str,input().split())
        new_first = second[0]+first[1:]
        new_second = first[0] + second[1:]
        results.append([new_first,new_second])
    for result in results:
        print(result[0],result[1])

if __name__ == "__main__":
    main()