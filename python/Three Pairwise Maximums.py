def main():
    t = int(input())
    results = []
    for _ in range(t):
        x,y,z = map(int,input().split())
        if (x == y and z <= x) or (x == z and y <= x) or (y == z and x <= y):
            results.append("YES")
            a = min(x, y, z)
            b = min(x, y, z)
            c = max(x, y, z)
            results.append(f"{a} {b} {c}")
        else:
            results.append("NO")
        
    for result in results:
        print(result)

if __name__ == '__main__':
    main()