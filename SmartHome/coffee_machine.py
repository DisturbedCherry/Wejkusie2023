from collections import Counter
from datetime import datetime, time, timedelta

def round_to_nearest_hour(time_str):
    time_format = "%H:%M"
    time_obj = datetime.strptime(time_str, time_format)
    rounded_time = (time_obj + timedelta(minutes=30)).replace(minute=0)
    return rounded_time.strftime(time_format)

with open("coffee_machine_data.csv", 'r') as file:
    data = [line[:-1].split(';') for line in file][1:]

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    for day in days:
        temp = [list for list in data if list[1] == day]
        temp_copy = [value.copy() for value in temp]
        # print(temp)

        time_format = "%H:%M"
        time_deltas = [datetime.strptime(value[2], time_format) - datetime.strptime('00:00', time_format) for value in temp]
        for value in temp_copy:
            value[2] = round_to_nearest_hour(value[2])
        # print(temp_copy)


        counter = Counter(tuple(sublist[1:4]) for sublist in temp_copy)
        repeating_lists = [list(sublist) for sublist, count in counter.items() if count >= 3]
        for sublist in repeating_lists:
            print(sublist)
