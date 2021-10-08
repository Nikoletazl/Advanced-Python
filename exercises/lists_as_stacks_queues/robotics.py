import math
from collections import deque


class Robot:
    def __init__(self, name, process_time):
        self.name = name
        self.process_time = process_time
        self.busy_until = 0


def get_seconds_from_time(time):
    hours, minutes, seconds = [int(x) for x in time.split(":")]
    return hours * 60 * 60 + minutes * 60 + seconds


def get_time_from_seconds(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // 3600
    minutes = math.floor((seconds / 60) % 60)
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots = []
robots_input = input().split(";")
for robots_input in robots_input:
    robots_name, processing_time = robots_input.split("-")
    robots.append(Robot(robots_name, int(processing_time)))

start_time_in_sec = get_seconds_from_time(input())
items = deque()

while True:
    item = input()
    if item == "End":
        break
    items.append(item)

while items:
    curr_item = items.popleft()
    start_time_in_sec += 1
    found_robot = False
    for robot in robots:
        if start_time_in_sec >= robot.busy_until:
            robot.busy_until = start_time_in_sec + robot.process_time
            found_robot = True
            print(f"{robot.name} - {curr_item} [{get_time_from_seconds(start_time_in_sec)}]")
            break
    if not found_robot:
        items.append(curr_item)