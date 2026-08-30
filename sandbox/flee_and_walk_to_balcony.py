import mgba
import time

def handle_battle_if_present():
    print("Encountered wild battle! Escaping...")
    # Stand still and press A to advance any appeared text
    for _ in range(3):
        mgba.press_buttons(["A"])
        time.sleep(0.8)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    # Select RUN (Down, Right, A)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    # Dismiss "Got away safely!"
    mgba.press_buttons(["B"])
    time.sleep(0.8)

def move_safe(step, target_x, target_y):
    pos_before = mgba.get_coordinates()
    print(f"Moving {step} from {pos_before} towards ({target_x}, {target_y})...")
    mgba.press_buttons([step])
    time.sleep(0.5)
    pos_after = mgba.get_coordinates()
    
    attempts = 0
    while (pos_after['x'] != target_x or pos_after['y'] != target_y) and attempts < 4:
        if pos_before == pos_after:
            print("Did not move. Attempting battle escape...")
            handle_battle_if_present()
        else:
            print(f"Moved but not to target. Current: {pos_after}. Escaping battle/retrying...")
            handle_battle_if_present()
            
        mgba.press_buttons([step])
        time.sleep(0.5)
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    print(f"Finished step. Current position: {pos_after}")
    return pos_after

# 1. Escape the current wild Ponyta battle
print("Fleeing current wild Ponyta battle...")
# Press A to advance "appeared!" text
mgba.press_buttons(["A"])
time.sleep(1.5)
# Press A to advance "Go! SHELLBY!" text
mgba.press_buttons(["A"])
time.sleep(2.5)
# Select RUN (Down, Right, A)
mgba.press_buttons(["Down", "Right", "A"])
time.sleep(1.5)
# Dismiss "Got away safely!"
mgba.press_buttons(["B"])
time.sleep(0.8)

# 2. Verify we are in the overworld and continue path to balcony
print("Overworld reached. Current position:", mgba.get_coordinates())

# From current (27, 16) to (19, 18) balcony drop
path = [
    # Walk Left along Row 16 to Column 21
    ("Left", 26, 16), ("Left", 25, 16), ("Left", 24, 16), ("Left", 23, 16), ("Left", 22, 16), ("Left", 21, 16),
    # Walk DOWN Column 21 through open balcony gates (21, 17) to Row 18
    ("Down", 21, 17), ("Down", 21, 18),
    # Walk Left to balcony drop warp at (19, 18)
    ("Left", 20, 18), ("Left", 19, 18)
]

for step, x, y in path:
    move_safe(step, x, y)

print("Arrived at balcony drop! Current position:", mgba.get_coordinates())
