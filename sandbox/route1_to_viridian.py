import mgba
import time
from PIL import Image

def run_away():
    print("Encountered something! Attempting to run away...")
    # Press B to clear any text/dialogue first
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    # Press Right, Down, A to select RUN
    mgba.press_buttons(["Right", "Down", "A"])
    time.sleep(1.0)
    # Press B to dismiss any failure or text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)

# Target path to Viridian City transition
# From current position (9, 26)
path = [
    # Walk right to Col 12
    (10, 26), (11, 26), (12, 26),
    # Walk up to Row 21
    (12, 25), (12, 24), (12, 23), (12, 22), (12, 21),
    # Walk left to Col 2
    (11, 21), (10, 21), (9, 21), (8, 21), (7, 21), (6, 21), (5, 21), (4, 21), (3, 21), (2, 21),
]

# Add vertical path up to Row 0
for y in range(20, -1, -1):
    path.append((2, y))

print(f"Path initialized with {len(path)} steps.")

current_target_index = 0
stuck_counter = 0
last_pos = mgba.get_coordinates()

while current_target_index < len(path):
    target_pos = path[current_target_index]
    pos = mgba.get_coordinates()
    print(f"Current pos: {pos}, Target: {target_pos}, Index: {current_target_index}/{len(path)}")
    
    # Check if we transitioned to Viridian City or Pallet Town unexpectedly
    # (Viridian City has different map, get_coordinates might change or wrap)
    # In Pokémon Blue, transitioning to a new map resets coordinates or we are on a new map.
    # Let's check if we reached y <= 0 or if coordinates jump
    if pos['y'] == 0 and target_pos[1] == 0:
        # We are at the very top of Route 1, let's step UP to transition
        print("At the top of Route 1, transitioning to Viridian City...")
        mgba.press_buttons(["Up"])
        time.sleep(1.0)
        break

    if pos['x'] == target_pos[0] and pos['y'] == target_pos[1]:
        # We reached the target!
        current_target_index += 1
        stuck_counter = 0
        last_pos = pos
        continue
        
    # Determine direction to target
    dx = target_pos[0] - pos['x']
    dy = target_pos[1] - pos['y']
    
    # We should only move 1 tile at a time
    if abs(dx) + abs(dy) > 1:
        # We are far from target, maybe we got pushed or transitioned?
        # If we are close, let's re-align. If we are completely elsewhere, let's stop and inspect.
        print(f"Warning: Distance to target is too large ({dx}, {dy}).")
        # Check if we are actually at a future step in the path
        found_future = False
        for i in range(current_target_index + 1, min(current_target_index + 5, len(path))):
            if pos['x'] == path[i][0] and pos['y'] == path[i][1]:
                print(f"Found ourselves at future step {i}!")
                current_target_index = i
                found_future = True
                break
        if found_future:
            continue
            
    # Move towards target
    btn = None
    if dx > 0:
        btn = "Right"
    elif dx < 0:
        btn = "Left"
    elif dy > 0:
        btn = "Down"
    elif dy < 0:
        btn = "Up"
        
    if btn:
        mgba.press_buttons([btn])
        time.sleep(0.3)
        
    # Check if we successfully moved
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        stuck_counter += 1
        print(f"Stuck count: {stuck_counter}")
        if stuck_counter >= 3:
            # We are stuck, likely in a wild encounter or blocked by an NPC/obstacle
            run_away()
            stuck_counter = 0
    else:
        stuck_counter = 0

print("Finished script execution.")
pos = mgba.get_coordinates()
print(f"Final position: {pos}")
