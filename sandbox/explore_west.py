import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

def step_to(target_x, target_y):
    pos = mgba.get_coordinates()
    print(f"Moving towards ({target_x}, {target_y}) from {pos}")
    
    # Try simple horizontal/vertical movement
    while pos['x'] != target_x or pos['y'] != target_y:
        dx = target_x - pos['x']
        dy = target_y - pos['y']
        
        # Decide direction
        if dx != 0:
            btn = 'Right' if dx > 0 else 'Left'
            target_step = (pos['x'] + (1 if dx > 0 else -1), pos['y'])
        else:
            btn = 'Down' if dy > 0 else 'Up'
            target_step = (pos['x'], pos['y'] + (1 if dy > 0 else -1))
            
        mgba.press_buttons([btn])
        time.sleep(0.3)
        
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == target_step[0] and new_pos['y'] == target_step[1]:
            pos = new_pos
        else:
            print(f"Blocked at {pos} trying to go to {target_step}. Checking for battle...")
            time.sleep(0.5)
            pos_check = mgba.get_coordinates()
            if pos_check == new_pos:
                run_from_battle()
                pos = mgba.get_coordinates()
            else:
                pos = new_pos
                
# Starting position: (26, 26)
# 1. Walk to the gap at (12, 12)
step_to(12, 12)

# 2. Walk Left to (10, 12)
step_to(10, 12)

# 3. Walk Down column 10 to (10, 14)
step_to(10, 14)

# 4. Explore walking Left from column 10 on row 14
print("Exploring walking Left from (10, 14)...")
for x in range(9, 1, -1):
    pos = mgba.get_coordinates()
    mgba.press_buttons(["Left"])
    time.sleep(0.3)
    new_pos = mgba.get_coordinates()
    if new_pos['x'] < pos['x']:
        print(f"Moved Left to {new_pos}")
    else:
        print(f"Blocked at {pos} trying to move Left")
        # Check battle
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            run_from_battle()
            break
        else:
            break

print("Final position:", mgba.get_coordinates())
