import time

def timer():
    Time = (int(input("Enter your time with minute : ")))*60

    for i in range(Time,0,-1):
        Second = i%60
        Minutes = (i//60)%60
        Hours = i//3600
        print(f"\r{Hours:02}:{Minutes:02}:{Second:02}", end="")
        time.sleep(1)

    print("\nTime over ")

