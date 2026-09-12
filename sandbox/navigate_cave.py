import mgba
import time

def flee_if_battle():
    mgba.press_buttons([
        "A", "sleep 150", "B", "sleep 150", "B", "sleep 150",
        "Down", "Right", "A", "sleep 350",
        "B", "sleep 150", "B", "sleep 150"
    ])

def step(dir_name):
    start = mgba.get_coordinates()
    for _ in range(3):
        mgba.press_buttons([dir_name, "sleep 150"])
        cur = mgba.get_coordinates()
        if cur != start:
            return True, cur
        flee_if_battle()
        cur = mgba.get_coordinates()
        if cur != start:
            return True, cur
    return False, start

pos = mgba.get_coordinates()
print("Starting pos:", pos)

# Let's walk Up to (24, 11), then Left towards (20, 11) and see how far west we can go on Row 11
# Step Up 2 to (24, 11)
for i in range(2):
    ok, pos = step("Up")
    print(f"Up -> {pos}")

# Step Left up to 12 times to see where Row 11 leads
for i in range(12):
    ok, pos = step("Left")
    print(f"Left {i+1} -> {ok}, {pos}")
    if not ok:
        break

print("Current pos:", mgba.get_coordinates())
