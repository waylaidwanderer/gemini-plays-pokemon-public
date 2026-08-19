import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# We are at (2, 7) inside Mansion 1F.
# Step 1: Walk UP column 3 to stairs at (3, 2)
path_1f = [
    ('Right', 3, 7),
    ('Up', 3, 6), ('Up', 3, 5), ('Up', 3, 4), ('Up', 3, 3), ('Up', 3, 2)
]

print("Walking to 1F/2F stairs...")
for btn, tx, ty in path_1f:
    pos = mgba.get_coordinates()
    print(f"1F: At {pos}, pressing {btn} to reach ({tx}, {ty})")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if tx == 3 and ty == 2:
        time.sleep(1.5) # Wait for warp
        print("Warped to 2F! Position:", mgba.get_coordinates())
        break
    if new_pos['x'] == tx and new_pos['y'] == ty:
        continue
    else:
        print(f"Failed to reach ({tx}, {ty}), checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()

# Step 2: On 2F, walk from (3, 3) to 3F stairs at (7, 7)
path_2f = [
    ('Down', 3, 4), ('Down', 3, 5), ('Down', 3, 6), ('Down', 3, 7),
    ('Right', 4, 7), ('Right', 5, 7), ('Right', 6, 7), ('Right', 7, 7)
]

print("Walking to 2F/3F stairs...")
for btn, tx, ty in path_2f:
    pos = mgba.get_coordinates()
    print(f"2F: At {pos}, pressing {btn} to reach ({tx}, {ty})")
    mgba.press_buttons([btn])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if tx == 7 and ty == 7:
        time.sleep(1.5) # Wait for warp
        print("Warped to 3F! Position:", mgba.get_coordinates())
        break
    if new_pos['x'] == tx and new_pos['y'] == ty:
        continue
    else:
        print(f"Failed to reach ({tx}, {ty}), checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()

# Step 3: On 3F, walk from (7, 7) to switch at (2, 12) using BFS
def is_walkable_3f(x, y):
    if x == 2 and y == 11: return False
    if x == 5 and y == 3: return False
    
    # Avoid the doormat exit warp tiles on 3F
    if y == 7 and (x == 2 or x == 3): return False
    
    # Wall on row 8 at columns 2, 3, 4 and columns 6 to 23
    if y == 8 and 2 <= x <= 4: return False
    if y == 8 and 6 <= x <= 23: return False
    
    # Closed shutter gates on row 4
    if y == 4 and (6 <= x <= 7 or 10 <= x <= 11 or x == 8 or x == 12): return False
    if x == 9 and y == 4: return False
    
    if not (2 <= x <= 25 and 3 <= y <= 16):
        return False
    return True

def find_path(start, target):
    queue = [[start]]
    visited = {start}
    while queue:
        path = queue.pop(0)
        curr = path[-1]
        if curr == target:
            return path
        for dx, dy, btn in [(0, -1, 'Up'), (0, 1, 'Down'), (-1, 0, 'Left'), (1, 0, 'Right')]:
            nxt = (curr[0] + dx, curr[1] + dy)
            if nxt == target or (is_walkable_3f(nxt[0], nxt[1]) and nxt not in visited):
                visited.add(nxt)
                queue.append(path + [nxt])
    return None

def get_button(curr, nxt):
    dx = nxt[0] - curr[0]
    dy = nxt[1] - curr[1]
    if dx == 1: return 'Right'
    if dx == -1: return 'Left'
    if dy == 1: return 'Down'
    if dy == -1: return 'Up'
    return None

target = (2, 12)
print(f"Starting BFS smart walk on 3F to switch target {target}...")

button_count = 0

while True:
    pos = mgba.get_coordinates()
    curr = (pos['x'], pos['y'])
    
    # Make sure we didn't warp out by accident
    if curr[1] > 20 or curr[0] > 20:
        # We are on 1F, 2F, or 3F. We should still be inside.
        pass
    else:
        # If we are on Cinnabar Island (20x20 map)
        if curr[0] < 20 and curr[1] < 20 and curr != (2, 12): # check we aren't at target
            print("Warped out by accident! Position:", curr)
            break
            
    if curr == target:
        print("Arrived at target position!")
        break
        
    path = find_path(curr, target)
    if not path or len(path) < 2:
        print(f"No path found from {curr} to {target}!")
        break
        
    nxt = path[1]
    btn = get_button(curr, nxt)
    print(f"3F: At {curr}, BFS Next Step: {btn} to {nxt}")
    
    mgba.press_buttons([btn])
    button_count += 1
    time.sleep(0.3)
    
    if button_count >= 80:
        print("Approaching execution limit, pausing script.")
        break
        
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == nxt[0] and new_pos['y'] == nxt[1]:
        continue
    else:
        print("Failed step. Checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            time.sleep(1)
        else:
            print("Position changed, continuing...")

# Step 5: Toggle switch at (2, 11)
if mgba.get_coordinates() == {'x': 2, 'y': 12}:
    print("Facing UP towards the switch...")
    mgba.press_buttons(["Up", "sleep 300"])
    print("Interacting with Mewtwo statue...")
    mgba.press_buttons(["A", "sleep 1000"]) # open text box
    print("Pressing YES...")
    mgba.press_buttons(["A", "sleep 1000"]) # select YES
    print("Dismissing final text...")
    mgba.press_buttons(["A", "sleep 500"]) # dismiss dialogue
    print("Switch successfully toggled!")

print("Final position:", mgba.get_coordinates())
