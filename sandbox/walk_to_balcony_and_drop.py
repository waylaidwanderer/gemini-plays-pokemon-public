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
            # We didn't move! Likely in a battle.
            print("Did not move. Attempting battle escape...")
            handle_battle_if_present()
        else:
            # We moved but to a different tile (maybe bumped or in battle)
            print(f"Moved but not to target. Current: {pos_after}. Escaping battle/retrying...")
            handle_battle_if_present()
            
        # Retry the step
        mgba.press_buttons([step])
        time.sleep(0.5)
        pos_after = mgba.get_coordinates()
        attempts += 1
        
    print(f"Finished step. Current position: {pos_after}")
    return pos_after

# Starting position: (10, 9) on 3F West
print("Starting walk to balcony drop on 3F East...")
print("Current position:", mgba.get_coordinates())

path = [
    # 1. Walk DOWN Column 10 to Row 11
    ("Down", 10, 10), ("Down", 10, 11),
    # 2. Walk Right to Column 12 (gate is open in State A)
    ("Right", 11, 11), ("Right", 12, 11),
    # 3. Walk UP Column 12 to Row 3
    ("Up", 12, 10), ("Up", 12, 9), ("Up", 12, 8), ("Up", 12, 7), ("Up", 12, 6), ("Up", 12, 5), ("Up", 12, 4), ("Up", 12, 3),
    # 4. Walk Right along Row 3 to Column 25
    ("Right", 13, 3), ("Right", 14, 3), ("Right", 15, 3), ("Right", 16, 3), ("Right", 17, 3), ("Right", 18, 3), ("Right", 19, 3), ("Right", 20, 3), ("Right", 21, 3), ("Right", 22, 3), ("Right", 23, 3), ("Right", 24, 3), ("Right", 25, 3),
    # 5. Walk DOWN Column 25 to Row 16 (gate at 25,13 is open in State A)
    ("Down", 25, 4), ("Down", 25, 5), ("Down", 25, 6), ("Down", 25, 7), ("Down", 25, 8), ("Down", 25, 9), ("Down", 25, 10), ("Down", 25, 11), ("Down", 25, 12), ("Down", 25, 13), ("Down", 25, 14), ("Down", 25, 15), ("Down", 25, 16),
    # 6. Walk Left along Row 16 to Column 21
    ("Left", 24, 16), ("Left", 23, 16), ("Left", 22, 16), ("Left", 21, 16),
    # 7. Walk DOWN Column 21 through open balcony gates (21, 17) to Row 18
    ("Down", 21, 17), ("Down", 21, 18),
    # 8. Walk Left to balcony drop warp at (19, 18)
    ("Left", 20, 18), ("Left", 19, 18)
]

for step, x, y in path:
    move_safe(step, x, y)

print("Arrived at balcony drop! Current position:", mgba.get_coordinates())
