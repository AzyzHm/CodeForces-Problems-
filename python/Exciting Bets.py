def solver(a:int,b:int)->list:
    return [0,0] if a==b else [abs(a-b),min(a%abs(a-b),abs(a-b)-a%abs(a-b))]
def main():
    t = int(input())
    tests = []
    for i in range(t):
        a,b = map(int,input().split())
        tests.append([a,b])
    for test in tests:
        print(*solver(*test))
    
if __name__ == "__main__":
    main()