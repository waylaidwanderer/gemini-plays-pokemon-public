import mgba
import time

def flee_if_battle():
    # Try dismissing any text and running
    mgba.press_buttons([
        "A", "sleep 150", "B", "sleep 150", "B", "sleep 150",
        "Down", "Right", "A", "sleep 350",
        "B", "sleep 150", "B", "sleep 150"
    ])

def step(dir_name):
    start_pos = mgba.get_coordinates()
    for attempt in range(4):
        mgba.press_buttons([dir_name, "sleep 150"])
        cur_pos = mgba.get_coordinates()
        if cur_pos != start_pos:
            return cur_pos
        # If position didn't change, we might be in battle or bumped a wall
        flee_if_battle()
        cur_pos = mgba.get_coordinates()
        # If position changed or battle cleared, try step again if we didn't move
    return mgba.get_coordinates()

pos = mgba.get_coordinates()
print(f"Start: {pos}")
for i in range(4):
    pos = step("Down")
    print(f"Step Down {i+1}: {pos}")

