import time
import datetime

count = 880
start_time_str = "20250411 09:40:54.000000"

start_time = datetime.datetime.strptime(start_time_str, "%Y%m%d %H:%M:%S.%f")

with open("times.csv", "w") as file:
    for i in range(count):
        current_time = start_time + datetime.timedelta(seconds=5 * i)
        timestamp_str = current_time.strftime("%Y%m%d %H:%M:%S.") + f"{current_time.microsecond:06d}"[:5]
        file.write(timestamp_str + "\n")
        
print("Timeshift Done")