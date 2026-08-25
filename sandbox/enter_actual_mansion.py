import mgba
import time

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        mgba.press_buttons([direction])
        time.sleep(0.3)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.2)
    return False

# Starting inside Cinnabar Lab at (2, 3)
# 1. Walk down to exit the Lab
steps_exit_lab = [
    ("Down", {"x": 2, "y": 4}),
    ("Down", {"x": 2, "y": 5}),
    ("Down", {"x": 2, "y": 6}),
    ("Down", {"x": 2, "y": 7}),
]

success = True
for direction, coords in steps_exit_lab:
    if not walk_step(direction, coords):
        success = False
        break

if success:
    print("Reached exit doormat of Cinnabar Lab! Exiting...")
    mgba.press_buttons(["Down"])
    time.sleep(1.5) # Wait for overworld load
    pos = mgba.get_coordinates()
    print(f"Exited Cinnabar Lab! Current coordinates: {pos}")
    
    # 2. Walk around the door warp at (6, 9) on Cinnabar Island to reach (6, 3)
    steps_outside = [
        ("Right", {"x": 7, "y": 10}),
        ("Up", {"x": 7, "y": 9}),
        ("Up", {"x": 7, "y": 8}),
        ("Left", {"x": 6, "y": 8}), # Successfully bypassed the Lab door warp at (6, 9)!
        ("Up", {"x": 6, "y": 7}),
        ("Up", {"x": 6, "y": 6}),
        ("Up", {"x": 6, "y": 5}),
        ("Up", {"x": 6, "y": 4}),
        ("Up", {"x": 6, "y": 3}),
    ]
    
    for d, c in steps_outside:
        if not walk_step(d, c):
            success = False
            break
            
    if success:
        print("Reached actual Pokémon Mansion entrance at (6, 3)! Entering...")
        mgba.press_buttons(["Up"])
        time.sleep(1.5) # Wait for map transition
        pos = mgba.get_coordinates()
        print(f"Entered actual Pokémon Mansion 1F West! Landing position: {pos}")
    else:
        print("Failed to reach Mansion entrance.")
else:
    print("Failed to exit Cinnabar Lab.")
