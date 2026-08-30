import mgba
import time

def handle_battle_if_present():
    print("Checking/handling wild battle...")
    for _ in range(3):
        mgba.press_buttons(["A"])
        time.sleep(0.8)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    mgba.press_buttons(["B"])
    time.sleep(0.8)

def move_safe(step, target_x, target_y):
    attempts = 0
    while True:
        pos_before = mgba.get_coordinates()
        print(f"Moving {step} from {pos_before} towards ({target_x}, {target_y})...")
        mgba.press_buttons([step])
        time.sleep(0.5)
        pos_after = mgba.get_coordinates()
        
        # True warp check
        if abs(pos_after['x'] - pos_before['x']) > 2 or abs(pos_after['y'] - pos_before['y']) > 2:
            print(f"WARPED! From {pos_before} to {pos_after}")
            return pos_after
            
        if pos_after['x'] == target_x and pos_after['y'] == target_y:
            print(f"Finished step. Current position: {pos_after}")
            return pos_after
            
        print(f"Moved but not to target. Current: {pos_after}. Escaping battle/retrying...")
        handle_battle_if_present()
        attempts += 1
        if attempts >= 4:
            print("Failed to reach target after 4 attempts.")
            return pos_after

# Starting from current (21, 6) in State B
# Walk to switch at (2, 6)
path_to_switch = [
    # Walk Left along Row 3 (since we are at y=6, wait, we are at (21,6) so we should go Up to row 3 first)
    ("Up", 21, 5),
    ("Up", 21, 4),
    ("Up", 21, 3),
    # Walk Left along Row 3 to Column 10
    ("Left", 20, 3),
    ("Left", 19, 3),
    ("Left", 18, 3),
    ("Left", 17, 3),
    ("Left", 16, 3),
    ("Left", 15, 3),
    ("Left", 14, 3),
    ("Left", 13, 3),
    ("Left", 12, 3),
    ("Left", 11, 3),
    ("Left", 10, 3),
    # Walk UP Column 10 to Row 2
    ("Up", 10, 2),
    # Walk Left along Row 2 to Column 4
    ("Left", 9, 2),
    ("Left", 8, 2),
    ("Left", 7, 2),
    ("Left", 6, 2),
    ("Left", 5, 2),
    ("Left", 4, 2),
    # Walk DOWN Column 4 to Row 5
    ("Down", 4, 3),
    ("Down", 4, 4),
    ("Down", 4, 5),
    # Walk Left to Column 2 Row 6
    ("Left", 3, 5),
    ("Down", 3, 6),
    ("Left", 2, 6)
]

print("Walking to switch at (2, 5)...")
for step, x, y in path_to_switch:
    pos = mgba.get_coordinates()
    if pos['y'] > 20:
        print("We warped! Stopping.")
        break
    move_safe(step, x, y)

pos_switch = mgba.get_coordinates()
if pos_switch == {'x': 2, 'y': 6}:
    print("Arrived at (2, 6). Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Let's perform a step-by-step switch interaction with screenshots!
    print("A-press 1 (interact)...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.take_screenshot() # Should show "A secret switch!"
    
    print("A-press 2 (advance to menu)...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.take_screenshot() # Should show YES/NO menu
    
    print("A-press 3 (select YES)...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.take_screenshot() # Should show "Who wouldn't?"
    
    print("A-press 4 (dismiss textbox)...")
    mgba.press_buttons(["A"])
    time.sleep(2.5)
    mgba.take_screenshot() # Should show overworld (mansion in State A)
    
    print("Switch dialogue probe complete.")
else:
    print("Failed to reach switch.")

mgba.take_screenshot()
