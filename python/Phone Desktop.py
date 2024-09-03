import math

def main():
    t = int(input())
    results = []
    for _ in range(t):
        x, y = map(int, input().split())
        screens_for_2x2 = math.ceil(y / 2)
        remaining_cells = (screens_for_2x2 * 15) - (y * 4)
        
        remaining_1x1 = max(0, x - remaining_cells)
        screens_for_1x1 = math.ceil(remaining_1x1 / 15)
        
        total_screens = screens_for_2x2 + screens_for_1x1
        results.append(total_screens)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()