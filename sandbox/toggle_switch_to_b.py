import mgba
import time

def handle_battle():
    print("Coordinates did not change. Likely a battle! Attempting to flee...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_step(tx, ty, direction):
    attempts = 0
    while attempts < 10:
        pos = mgba.get_coordinates()
        if pos['x'] == tx and pos['y'] == ty:
            return True
            
        mgba.press_buttons([direction])
        time.sleep(0.55)
        new_pos = mgba.get_coordinates()
        
        if new_pos == pos:
            print(f"Bumped at {pos} going {direction}. Attempting battle escape...")
            handle_battle()
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        else:
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
        attempts += 1
    return False

# Starting at (4, 11) on 2F West inside the Mansion
pos = mgba.get_coordinates()
print("Starting toggle_switch_to_b from:", pos)

if pos['x'] == 4 and pos['y'] == 11:
    # Walk left to (2, 11)
    walk_step(3, 11, 'Left')
    walk_step(2, 11, 'Left')

# Standing at (2, 11), face UP and press A to toggle switch to State B
pos = mgba.get_coordinates()
if pos['x'] == 2 and pos['y'] == 11:
    print("Facing UP and toggling switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B"])
    time.sleep(1.5)

print("Final coordinates after script:", mgba.get_coordinates())
mgba.take_screenshot()
