import mgba
import time

def step_to(tx, ty):
    print(f"Moving step-by-step to ({tx}, {ty})...")
    while True:
        curr = mgba.get_coordinates()
        cx, cy = curr['x'], curr['y']
        if cx == tx and cy == ty:
            print(f"Arrived at ({tx}, {ty})")
            return True
            
        # Determine button direction
        if cx < tx: btn = "Right"
        elif cx > tx: btn = "Left"
        elif cy < ty: btn = "Down"
        else: btn = "Up"
        
        mgba.press_buttons([btn])
        time.sleep(0.45)
        
        new_pos = mgba.get_coordinates()
        if new_pos['x'] == cx and new_pos['y'] == cy:
            # Coordinates didn't change! We are in a battle.
            print("Position unchanged. Running from battle...")
            mgba.press_buttons(["Down", "Right", "A"])
            time.sleep(1.5)
            for _ in range(5):
                mgba.press_buttons(["B"])
                time.sleep(0.1)
            time.sleep(0.5)

# We are currently at (17, 22) in the overworld.
# 1. Walk to the West Stairs on Column 6
step_to(17, 20)
step_to(6, 20)
step_to(6, 16) # Climb West Stairs to plateau

# 2. Walk RIGHT across the plateau (staying on Row 16)
step_to(21, 16)

# 3. Walk DOWN Column 21 descending East Stairs to ground level
step_to(21, 18)

# 4. Walk to (19, 24) directly above the teeth
step_to(19, 18)
step_to(19, 24)

# 5. Face DOWN
print("Facing DOWN...")
mgba.press_buttons(["Down"])
time.sleep(0.5)

# 6. Press A to pick up the Gold Teeth
print("Pressing A to pick up the Gold Teeth...")
mgba.press_buttons(["A"])
time.sleep(1.5)

# Clear dialogue "ACE picked up the GOLD TEETH!"
print("Clearing dialogue...")
mgba.press_buttons(["A"])
time.sleep(1.0)
mgba.press_buttons(["A"])
time.sleep(1.0)

final_pos = mgba.get_coordinates()
print("Position after retrieval attempt:", final_pos)
screenshot_path = mgba.take_screenshot()
print(f"Screenshot: {screenshot_path}")
