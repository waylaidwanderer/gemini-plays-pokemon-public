import mgba
import time

def is_walkable_1f(x, y):
    # Rubble on west side
    if y == 8 and 8 <= x <= 11: return False
    if y == 9 and 8 <= x <= 9: return False
    
    # West side computers
    if x == 8 and y in [10, 12, 14, 16]: return False
    
    # Column 9 vertical wall on rows 4 to 7
    if x == 9 and 4 <= y <= 7: return False
    
    # Column 11 vertical wall on all rows except row 12
    if x == 11 and y != 12: return False
    
    # Closed shutter gates on row 13 at columns 11 to 14
    if y == 13 and 11 <= x <= 14: return False
    
    # Closed shutter gates on row 13 at columns 19 to 21
    if y == 13 and 19 <= x <= 21: return False
    
    # Wall on row 13 at columns 26 to 28
    if y == 13 and x >= 26: return False
    # Wall on row 17 at columns 26 to 28
    if y == 17 and x >= 26: return False
    
    # Closed gate at (19, 8) in State A
    if x == 19 and y == 8: return False
    
    # Rubble on row 14 at columns 19 to 21
    if y == 14 and 19 <= x <= 21: return False
    
    # Rubble in central area (continuous barrier)
    if y == 8 and 20 <= x <= 22: return False
    if y == 9 and 20 <= x <= 22: return False
    if y == 10 and 21 <= x <= 22: return False
    if y == 11 and 21 <= x <= 22: return False
    if y == 12 and 22 <= x <= 23: return False
    if y == 13 and 22 <= x <= 23: return False
    
    # Rubble at bottom-right
    if y == 14 and x >= 28: return False
    if y == 15 and x >= 28: return False
    if y == 18 and x >= 26: return False
    if y == 19 and x >= 28: return False
    
    # Map bounds
    if not (2 <= x <= 28 and 3 <= y <= 27):
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
            if nxt == target or (is_walkable_1f(nxt[0], nxt[1]) and nxt not in visited):
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

# Target: West side stairs at (5, 10)
target = (5, 10)
print(f"Starting BFS smart walk to 2F stairs {target}...")

button_count = 0

while True:
    pos = mgba.get_coordinates()
    curr = (pos['x'], pos['y'])
    
    if curr == target:
        print("Arrived at target stairs!")
        time.sleep(1.0)
        warp_pos = mgba.get_coordinates()
        print("Position after warp:", warp_pos)
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
        # Step succeeded. But wait! If target is (5, 10), stepping onto it warps us to 2F!
        if nxt == target:
            time.sleep(1.0)
            warp_pos = mgba.get_coordinates()
            print("Warped to 2F! Position:", warp_pos)
            break
        continue
    else:
        # Check if we warped on the last step
        if nxt == target:
            time.sleep(1.0)
            warp_pos = mgba.get_coordinates()
            print("Warped to 2F! Position:", warp_pos)
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
