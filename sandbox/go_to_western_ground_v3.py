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

# We are currently at (19, 19).
# 1. Walk to the Eastern Plateau East Stairs entrance
step_to(19, 18)
step_to(21, 18)
step_to(21, 17) # Climb stairs onto plateau

# 2. Walk LEFT across the plateau (staying on Row 17)
step_to(6, 17)

# 3. Walk DOWN Column 6 to descend the West Stairs
step_to(6, 19) # Steps onto West Stairs
step_to(6, 20) # Descends stairs onto western ground grass!

final_pos = mgba.get_coordinates()
print("Position inside Western Ground Level:", final_pos)
screenshot_path = mgba.take_screenshot()
print(f"Screenshot: {screenshot_path}")
