import mgba
import time

def run_from_battle():
    print("In battle! Running...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Right", "sleep 150", "Down", "sleep 150", "A", "sleep 600"])
    for _ in range(4):
        mgba.press_buttons(["B", "sleep 150"])

def walk_step(direction):
    pos_before = mgba.get_coordinates()
    mgba.press_buttons([direction, "sleep 150"])
    pos_after = mgba.get_coordinates()
    
    if pos_before == pos_after:
        mgba.press_buttons([direction, "sleep 150"])
        pos_after = mgba.get_coordinates()
        
        attempts = 0
        while pos_before == pos_after and attempts < 10:
            run_from_battle()
            mgba.press_buttons([direction, "sleep 150"])
            pos_after = mgba.get_coordinates()
            attempts += 1
    return pos_after

# Starting at (15, 6) on 2F East
print("Current position:", mgba.get_coordinates())

# Let's walk down Column 15 step by step
for i in range(6):
    pos = walk_step("Down")
    print(f"Step {i+1} Down: new position {pos}")
    # If the map changed, print it and break
    # (Since we don't have get_map_name in SDK directly, we can check if coordinates jumped significantly)
    
sc = mgba.take_screenshot()
print("Final screenshot saved:", sc)
