from common import load_file

read_lines = load_file()

starts, ends = [], []
for line in read_lines:
    start, end = line.strip().split("-")
    starts.append(start), ends.append(end)

reachable_rooms = dict()

for room in starts + ends:
    reachable_rooms[room] = []

for start_room, end_room in zip(starts, ends):
    if end_room not in reachable_rooms[start_room]:
        reachable_rooms[start_room].append(end_room)
    if start_room not in reachable_rooms[end_room]:
        reachable_rooms[end_room].append(start_room)

for room in starts + ends:
    reachable_rooms[room] = sorted(reachable_rooms[room])


def initiate_room_visit_count():
    room_visit_count = dict()
    for room in starts + ends:
        if room != "start" and room.islower():
            room_visit_count[room] = 0
    return room_visit_count


# Part 1
room_visit_count = initiate_room_visit_count()
n_possible_paths = 0
room_stack = [("start", room_visit_count)]
while room_stack:
    current_room, room_visit_count = room_stack.pop()
    for room in reachable_rooms[current_room]:
        if room == "end":
            n_possible_paths += 1
            continue
        elif room == "start":
            continue
        else:
            room_visit_count_sub = room_visit_count.copy()
            if room.islower():
                if room_visit_count[room] > 0:
                    continue
                room_visit_count_sub[room] += 1
            room_stack.append((room, room_visit_count_sub))

print(f"Answer part 1: {n_possible_paths}")


# Part 2
room_visit_count = initiate_room_visit_count()
n_possible_paths = 0
room_stack = [("start", room_visit_count)]
while room_stack:
    current_room, room_visit_count = room_stack.pop()
    for room in reachable_rooms[current_room]:
        if room == "end":
            n_possible_paths += 1
            continue
        elif room == "start":
            continue
        else:
            room_visit_count_sub = room_visit_count.copy()
            if room.islower():
                if max(room_visit_count.values()) > 1 and room_visit_count[room] > 0:
                    continue
                room_visit_count_sub[room] += 1
            room_stack.append((room, room_visit_count_sub))

print(f"Answer part 2: {n_possible_paths}")