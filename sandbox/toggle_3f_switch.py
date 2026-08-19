import mgba
import time

def is_walkable_3f(x, y):
    # Mewtwo statues
    if x == 2 and y == 11: return False
    if x == 5 and y == 3: return False
    
    # Closed shutter gates on row 4
    if y == 4 and (6 <= x <= 7 or 10 <= x <= 11 or x == 8 or x == 12): return False
    
    # Wall panels
    if x == 9 and y == 4: return False
    
    # Solid horizontal wall on row 8 separating upper hallway from lower area
    if y == 8 and 6 <= x <= 23: return False
    
    # Map bounds on 3F
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

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

# Target: standing south of the switch at (2, 12)
target = (2, 12)
print(f"Starting BFS smart walk to 3F switch target {target}...")

button_count = 0

while True:
    pos = mgba.get_coordinates()
    curr = (pos['x'], pos['y'])
    
    if curr == target:
        print("Arrived at target position!")
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
        print("Failed step. Checking for battle...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            time.sleep(1)
        else:
            print("Position changed, continuing...")

# Once at (2, 12), face UP, interact and press YES
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
