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

# Let's move Right 1 to (15, 11), then Down towards row 17
ok, pos = step("Right")
print(f"Right -> {pos}")

for i in range(8):
    ok, pos = step("Down")
    print(f"Down {i+1} -> {ok}, {pos}")
    if not ok:
        break

print("Pos at bottom:", pos)

# Now let's try moving Right along the bottom row (row 17?)
for i in range(15):
    ok, pos = step("Right")
    print(f"Right {i+1} -> {ok}, {pos}")
    if not ok:
        break

print("Final pos:", mgba.get_coordinates())
