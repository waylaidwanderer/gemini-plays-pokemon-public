import mgba
import time

def handle_battle_if_present():
    print("Detected block/battle. Fleeing...")
    # Clear "appeared!" text
    mgba.press_buttons(["B"])
    time.sleep(0.8)
    # Select RUN (Down, sleep, Right, sleep, A)
    mgba.press_buttons(["Down", "sleep 300", "Right", "sleep 300", "A"])
    time.sleep(2.0)
    # Clear "Got away safely!" text
    mgba.press_buttons(["B"])
    time.sleep(1.0)

# Full path from current (27, 9) on 3F East to (19, 18) balcony drop in State A
path = [
    (27, 9),
    (26, 9),
    (26, 10), (26, 11), (26, 12), (26, 13), (26, 14), (26, 15), (26, 16),
    (25, 16), (24, 16), (23, 16), (22, 16), (21, 16),
    (21, 17), (21, 18),
    (20, 18), (19, 18)
]

coord_to_index = {coord: i for i, coord in enumerate(path)}

def get_direction(curr, nxt):
    dx = nxt[0] - curr[0]
    dy = nxt[1] - curr[1]
    if dx == 1: return "Right"
    if dx == -1: return "Left"
    if dy == 1: return "Down"
    if dy == -1: return "Up"
    return None

print("Starting final path follower to the balcony drop from (27, 9)...")
max_button_presses = 100
button_count = 0

while button_count < max_button_presses:
    curr = mgba.get_coordinates()
    curr_tup = (curr['x'], curr['y'])
    
    # Check if we warped to B1F West (which would be at some coordinate with y >= 16 and x < 15, usually around 9,16 or 9,18 or similar)
    if curr_tup[1] == 16 and curr_tup[0] < 15:
        print("We successfully warped to B1F West! Current Position:", curr_tup)
        break
        
    if curr_tup == (19, 18):
        print("Arrived at balcony drop tile (19, 18). Triggering warp...")
        # Step onto the warp (or wait, the warp triggers immediately upon stepping onto (19, 18)!)
        # But let's take a step Left just in case
        mgba.press_buttons(["Left"])
        time.sleep(1.0)
        pos_after_warp = mgba.get_coordinates()
        print("New Position after warp step:", pos_after_warp)
        break
        
    if curr_tup not in coord_to_index:
        print(f"Off-path at {curr_tup}! Stopping.")
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
        # Check if we triggered a warp (coordinates jumped dramatically)
        if abs(pos_after['x'] - curr['x']) > 2 or abs(pos_after['y'] - curr['y']) > 2:
            print(f"WARPED! From {curr_tup} to {pos_after_tup}")
            break
            
        print(f"Movement failed. Still at {curr_tup}. Handling battle...")
        handle_battle_if_present()
        button_count += 4

final_pos = mgba.get_coordinates()
print("Final Position:", final_pos)
mgba.take_screenshot()
