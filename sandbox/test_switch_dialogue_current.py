import mgba
import time

def handle_any_menu_or_battle():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    # Simple check for dialogue/battle
    return False

def walk_step(direction, expected_coords):
    mgba.press_buttons([direction])
    time.sleep(0.45)
    pos = mgba.get_coordinates()
    print(f"Moved {direction}, expected: {expected_coords}, actual: {pos}")
    return pos == expected_coords

# Let's walk to (2, 12)
pos = mgba.get_coordinates()
print("Starting position:", pos)

if pos == {"x": 3, "y": 10}:
    walk_step("Down", {"x": 3, "y": 11})
    walk_step("Down", {"x": 3, "y": 12})
    walk_step("Left", {"x": 2, "y": 12})

pos = mgba.get_coordinates()
if pos == {"x": 2, "y": 12}:
    print("At (2, 12). Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    print("Pressing A for the first time...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img1 = mgba.take_screenshot()
    print("Screenshot 1 after first A:", img1)
    
    print("Pressing A for the second time...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img2 = mgba.take_screenshot()
    print("Screenshot 2 after second A:", img2)
    
    print("Pressing A for the third time (to confirm YES)...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img3 = mgba.take_screenshot()
    print("Screenshot 3 after third A:", img3)
    
    print("Pressing A for the fourth time (to dismiss text)...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    img4 = mgba.take_screenshot()
    print("Screenshot 4 after fourth A:", img4)
    
