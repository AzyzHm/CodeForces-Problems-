def main():
    t = int(input())
    results = []
    for _ in range(t):
        first_corner = list(map(int,input().split()))
        second_corner = list(map(int,input().split()))
        third_corner = list(map(int,input().split()))
        fourth_corner = list(map(int,input().split()))
        # if two corners have the same x or y we can't use them so we look for two diffrent ones
        if(first_corner[0] != second_corner[0] and first_corner[1] != second_corner[1]):
            area = abs(first_corner[0] - second_corner[0]) * abs(first_corner[1] - second_corner[1])
        elif(first_corner[0] != third_corner[0] and first_corner[1] != third_corner[1]):
            area = abs(first_corner[0] - third_corner[0]) * abs(first_corner[1] - third_corner[1])
        else:
            area = abs(first_corner[0] - fourth_corner[0]) * abs(first_corner[1] - fourth_corner[1])
        results.append(area)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()