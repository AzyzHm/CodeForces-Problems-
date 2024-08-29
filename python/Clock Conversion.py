def main():
    t = int(input())
    results = []
    for _ in range(t):
        s = input()
        hour , minute = s.split(":")
        hour = int(hour)
        if hour == 0:
            formatted_time = f"12:{minute} AM"
        elif hour < 12:
            formatted_time = f"{hour:02}:{minute} AM"
        elif hour == 12:
            formatted_time = f"12:{minute} PM"
        else:
            formatted_time = f"{hour - 12:02}:{minute} PM"
        results.append(formatted_time) 
    for result in results:
        print(result)


if __name__ == "__main__":
    main()