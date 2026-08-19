import mgba
import time

def is_walkable(x, y):
    # Rubble blocks on row 8, columns 8 to 11
    if y == 8 and 8 <= x <= 11:
        return False
    # Rubble blocks on row 9, columns 8 to 9
    if y == 9 and 8 <= x <= 9:
        return False
    # Closed shutter gates on row 13, columns 11 to 14
    if y == 13 and 11 <= x <= 14:
        return False
    # Closed shutter gates on row 7, columns 13 to 22
    if y == 7 and 13 <= x <= 22:
        return False
    # Vertical wall at column 13 on rows 8 to 12
    if x == 13 and 8 <= y <= 12:
        return False
    # Bound limits on western 1F
    if not (2 <= x <= 22 and 3 <= y <= 16):
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
            if nxt == target or (is_walkable(nxt[0], nxt[1]) and nxt not in visited):
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

# Target: 1F/2F stairs at (5, 10)
target = (5, 10)
print(f"Smart walk starting towards {target}...")

button_count = 0

while True:
    pos = mgba.get_coordinates()
    curr = (pos['x'], pos['y'])
    if curr == target:
        print("Arrived at target!")
        # Warp check
        time.sleep(1.0)
        warp_pos = mgba.get_coordinates()
        print("Warped position:", warp_pos)
        break
        
    path = find_path(curr, target)
    if not path or len(path) < 2:
        print(f"No path found from {curr} to {target}!")
        break
        
    nxt = path[1]
    btn = get_button(curr, nxt)
    print(f"At {curr}, path: {path[:4]}... Next Step: {btn} to {nxt}")
    
    # Take the step
    mgba.press_buttons([btn])
    button_count += 1
    time.sleep(0.3)
    
    # Check button limit
    if button_count >= 80:
        print("Approaching execution limit, pausing to save state.")
        break
        
    new_pos = mgba.get_coordinates()
    if new_pos['x'] == nxt[0] and new_pos['y'] == nxt[1]:
        # Step succeeded
        continue
    else:
        # Check for warp if target was (5, 10)
        if nxt == target:
            time.sleep(1.0)
            warp_pos = mgba.get_coordinates()
            print("Warp check after last step. Position:", warp_pos)
            break
            
        print("Failed step. Checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            time.sleep(1)
        else:
            print("Position changed, continuing...")
