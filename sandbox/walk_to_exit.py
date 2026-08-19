import mgba
import time

def is_walkable_east(x, y):
    # Rubble blocks on column 28
    if y == 14 and x >= 28: return False
    if y == 15 and x >= 28: return False
    if y == 18 and x >= 26: return False
    if y == 19 and x >= 28: return False
    
    # Walls on row 13 at columns 26 to 28
    if y == 13 and x >= 26: return False
    # Walls on row 17 at columns 26 to 28
    if y == 17 and x >= 26: return False
    
    # Closed shutter gates on row 13 at columns 11 to 14
    if y == 13 and 11 <= x <= 14: return False
    # Wall on column 11 on rows 14 to 26
    if x == 11 and 14 <= y <= 26: return False
    
    # Rubble in central area
    if y == 8 and 20 <= x <= 22: return False
    if y == 9 and 20 <= x <= 22: return False
    if y == 10 and 21 <= x <= 22: return False
    
    # Bound limits on eastern 1F
    if not (11 <= x <= 28 and 3 <= y <= 28):
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
            if nxt == target or (is_walkable_east(nxt[0], nxt[1]) and nxt not in visited):
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

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# Target: Exit at (26, 28)
target = (26, 28)
print(f"Starting BFS smart walk to exit {target}...")

button_count = 0

while True:
    pos = mgba.get_coordinates()
    curr = (pos['x'], pos['y'])
    
    # Check if we exited the Mansion (x coordinate resets or y coordinate is outside range)
    if curr[1] > 27 or curr[0] < 2:
        print("Warped out of Mansion! Position:", curr)
        break
        
    if curr == target:
        print("Arrived at target exit!")
        break
        
    path = find_path(curr, target)
    if not path or len(path) < 2:
        print(f"No path found from {curr} to {target}!")
        break
        
    nxt = path[1]
    btn = get_button(curr, nxt)
    print(f"At {curr}, BFS Next Step: {btn} to {nxt}")
    
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
        # Check if we exited on the last step
        if new_pos['y'] > 27 or new_pos['x'] < 2:
            print("Warped out of Mansion! Position:", new_pos)
            break
            
        print("Failed step. Checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            time.sleep(1)
        else:
            print("Position changed, continuing...")

print("Final position:", mgba.get_coordinates())
