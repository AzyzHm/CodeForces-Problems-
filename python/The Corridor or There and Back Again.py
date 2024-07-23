def find_minimum_rooms(n, room, seconds):
    min_room = 9999
    for i in range(n):
        if seconds[i] == 1:
            min_room = min(min_room, room[i])
        elif seconds[i]%2 == 0:
            min_room = min(min_room, room[i]+seconds[i]//2-1)
        else:
            min_room = min(min_room, room[i]+seconds[i]//2)
    return min_room
    
def main():
    t = int(input())
    tests = []
    for i in range(t):
        n = int(input())
        rooms = []
        seconds = []
        for i in range(n):
            d,s = map(int, input().split())
            rooms.append(d)
            seconds.append(s)
        tests.append([n, rooms, seconds])
    
    
    for test in tests:
        n, rooms, seconds = test
        print(find_minimum_rooms(n, rooms, seconds))
        
if __name__ == "__main__":
    main()