import mgba
import time

def handle_battle_if_present():
    print("Detected block. Fleeing battle...")
    # Clear "appeared!" text
    mgba.press_buttons(["B"])
    time.sleep(0.8)
    # Select RUN (Down, sleep, Right, sleep, A)
    mgba.press_buttons(["Down", "sleep 300", "Right", "sleep 300", "A"])
    time.sleep(2.0)
    # Clear "Got away safely!" text
    mgba.press_buttons(["B"])
    time.sleep(1.0)

# Full path from (25, 3) to (2, 6)
path = [
    (25, 3), (24, 3), (23, 3), (22, 3), (21, 3), (20, 3), (19, 3), (18, 3), (17, 3), (16, 3), (15, 3), (14, 3), (13, 3), (12, 3), (11, 3), (10, 3),
    (10, 2),
    (9, 2), (8, 2), (7, 2), (6, 2), (5, 2), (4, 2), (3, 2), (2, 2),
    (2, 3), (2, 4), (2, 5), (2, 6)
]

# Map coordinate to the direction to reach the next coordinate in the path
coord_to_index = {coord: i for i, coord in enumerate(path)}

def get_direction(curr, nxt):
    dx = nxt[0] - curr[0]
    dy = nxt[1] - curr[1]
    if dx == 1: return "Right"
    if dx == -1: return "Left"
    if dy == 1: return "Down"
    if dy == -1: return "Up"
    return None

print("Starting robust state-machine path follower to the switch...")
max_button_presses = 80
button_count = 0

while button_count < max_button_presses:
    curr = mgba.get_coordinates()
    curr_tup = (curr['x'], curr['y'])
    
    # If we reached the target
    if curr_tup == (2, 6):
        print("Arrived at (2, 6) successfully!")
        break
        
    if curr_tup not in coord_to_index:
        print(f"We are off-path at {curr_tup}! Attempting to get back...")
        # If we are at (26, 3), walk Left to get back on path
        if curr_tup == (26, 3):
            mgba.press_buttons(["Left"])
            time.sleep(0.6)
            button_count += 1
            continue
        # Otherwise, stop and let human inspect
        print("Unknown position. Stopping.")
        break
        
    curr_idx = coord_to_index[curr_tup]
    nxt_tup = path[curr_idx + 1]
    dir_to_go = get_direction(curr_tup, nxt_tup)
    
    print(f"Current: {curr_tup}, Next: {nxt_tup}. Moving {dir_to_go}...")
    mgba.press_buttons([dir_to_go])
    time.sleep(0.6)
    button_count += 1
    
    pos_after = mgba.get_coordinates()
    pos_after_tup = (pos_after['x'], pos_after['y'])
    
    if pos_after_tup == nxt_tup:
        print(f"Successfully moved to {pos_after_tup}")
    else:
        print(f"Movement failed. Still at {curr_tup}. Handling battle...")
        handle_battle_if_present()
        button_count += 4 # estimate buttons pressed to flee

# Now we are at (2, 6) facing UP (since we just walked DOWN from (2, 5)).
# Toggle the Mewtwo switch at (2, 5) to State A using exactly 4 A-presses
curr = mgba.get_coordinates()
if curr['x'] == 2 and curr['y'] == 6:
    print("Toggling Mewtwo switch at (2, 5) to State A...")
    # Stand at (2, 6) facing UP and press A 4 times with generous delays
    for i in range(1, 5):
        print(f"Pressing A ({i}/4)...")
        mgba.press_buttons(["A"])
        time.sleep(2.0)
        
    # Verify local state transition (State A blocks right movement at (2, 6))
    print("Verifying State A is active...")
    pos_before = mgba.get_coordinates()
    mgba.press_buttons(["Right"])
    time.sleep(0.6)
    pos_after = mgba.get_coordinates()
    if pos_before == pos_after:
        print("SUCCESS! State A is active (blocked at (2, 6))!")
    else:
        print(f"FAILED! Walked to {pos_after}. We are still in State B.")
        
mgba.take_screenshot()
