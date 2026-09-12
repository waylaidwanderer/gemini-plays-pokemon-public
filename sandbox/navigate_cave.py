import mgba
import time

def flee_if_battle():
    # Attempt to dismiss battle and run
    mgba.press_buttons([
        "A", "sleep 150", "B", "sleep 150", "B", "sleep 150",
        "Down", "Right", "A", "sleep 350",
        "B", "sleep 150", "B", "sleep 150"
    ])

def try_step(dir_name):
    # Returns (success, new_pos)
    old = mgba.get_coordinates()
    mgba.press_buttons([dir_name, "sleep 150"])
    new_pos = mgba.get_coordinates()
    if new_pos != old:
        return True, new_pos
    # If didn't move, check if battle
    flee_if_battle()
    new_pos = mgba.get_coordinates()
    if new_pos != old:
        return True, new_pos
    # Try one more time after fleeing
    mgba.press_buttons([dir_name, "sleep 150"])
    new_pos = mgba.get_coordinates()
    if new_pos != old:
        return True, new_pos
    return False, old

print("Starting position:", mgba.get_coordinates())

# From (24, 15), let's walk back up to (24, 12), then right to (26, 12), then down/explore
path_log = []
# Up 3 steps to (24, 12)
for i in range(3):
    ok, p = try_step("Up")
    path_log.append(("Up", ok, p))
    print(f"Up -> {p}")

# Right 2 steps to (26, 12)
for i in range(2):
    ok, p = try_step("Right")
    path_log.append(("Right", ok, p))
    print(f"Right -> {p}")

print("Current pos:", mgba.get_coordinates())
