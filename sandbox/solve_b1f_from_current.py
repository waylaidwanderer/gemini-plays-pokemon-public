import mgba
import time
from PIL import Image

def handle_any_menu_or_battle():
    time.sleep(0.15)
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    black_or_white = 0
    total_pixels = 0
    for y in range(115, 140):
        for x in range(10, 150):
            r, g, b = img_std.getpixel((x, y))[:3]
            total_pixels += 1
            is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
            if is_bw:
                black_or_white += 1
                
    percentage = black_or_white / total_pixels
    if percentage > 0.90:
        print(f"Menu/Dialogue detected! (B/W: {percentage*100:.2f}%)")
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
        # Check if still in battle
        scr_file2 = mgba.take_screenshot()
        img2 = Image.open(scr_file2)
        img_std2 = img2.resize((160, 144), Image.Resampling.NEAREST)
        black_or_white2 = 0
        for y in range(115, 140):
            for x in range(10, 150):
                r, g, b = img_std2.getpixel((x, y))[:3]
                is_bw = (r < 50 and g < 50 and b < 50) or (r > 200 and g > 200 and b > 200)
                if is_bw:
                    black_or_white2 += 1
        percentage2 = black_or_white2 / total_pixels
        
        if percentage2 > 0.90:
            print("Still in battle. Running...")
            mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
            time.sleep(1.5)
            # Dismiss run text
            for _ in range(4):
                mgba.press_buttons(["B"])
                time.sleep(0.3)
        return True
    return False

def walk_step(direction, expected_coords, retries=15):
    for i in range(retries):
        if handle_any_menu_or_battle():
            pos = mgba.get_coordinates()
            if pos == expected_coords:
                return True
        mgba.press_buttons([direction])
        time.sleep(0.45)
        pos = mgba.get_coordinates()
        if pos == expected_coords:
            print(f"Moved {direction}, current position: {pos}")
            return True
        print(f"Blocked or battle! Retrying {direction} to {expected_coords} (attempt {i+1}/{retries}), current: {pos}")
        time.sleep(0.3)
    return False

def run_steps(steps):
    for d, c in steps:
        if not walk_step(d, c):
            return False
    return True

# Ensure menu is closed
mgba.press_buttons(["B"])
time.sleep(0.3)

pos = mgba.get_coordinates()
print("Current position:", pos)

if pos == {"x": 10, "y": 5}:
    # Walk to Column 12 Row 5
    steps = [
        ("Right", {"x": 11, "y": 5}),
        ("Right", {"x": 12, "y": 5}),
    ]
    if not run_steps(steps):
        print("Failed to reach (12, 5)")
        exit(1)
    pos = mgba.get_coordinates()

# Now on (12, 5). Walk DOWN Column 12 to Row 11
if pos == {"x": 12, "y": 5}:
    print("Walking down Column 12 to Row 11...")
    steps = []
    for y in range(6, 12):
        steps.append(("Down", {"x": 12, "y": y}))
    if not run_steps(steps):
        print("Failed to reach (12, 11)")
        exit(1)
    pos = mgba.get_coordinates()

# Now on (12, 11). Test if we can walk LEFT across Column 9 gate on Row 11 (State A gate)
if pos == {"x": 12, "y": 11}:
    print("Testing crossing Row 11 gate LEFT to Column 8...")
    steps = [
        ("Left", {"x": 11, "y": 11}),
        ("Left", {"x": 10, "y": 11}),
        ("Left", {"x": 9, "y": 11}),
        ("Left", {"x": 8, "y": 11}),
    ]
    state_a_open = run_steps(steps)
    print("Row 11 Gate Open (State A):", state_a_open)
    pos = mgba.get_coordinates()

# If Row 11 Gate is open (meaning we are in State A), we must go back to 3F West to toggle it to State B!
if pos == {"x": 8, "y": 11} or state_a_open:
    print("Confirmed State A. Navigating back to the stairs at (22, 4) to go up...")
    # Walk back to (12, 11)
    steps = []
    for x in range(pos["x"] + 1, 13):
        steps.append(("Right", {"x": x, "y": 11}))
    # Walk up Column 12 to Row 5 (12, 5)
    for y in range(10, 4, -1):
        steps.append(("Up", {"x": 12, "y": y}))
    # Walk Right along Row 5 to Column 22 (22, 5)
    for x in range(13, 23):
        steps.append(("Right", {"x": x, "y": 5}))
        
    if not run_steps(steps):
        print("Failed to reach (22, 5)")
        exit(1)
    pos = mgba.get_coordinates()

    # Step UP onto stairs at (22, 4)
    if pos == {"x": 22, "y": 5}:
        print("Stepping UP onto B1F East stairs to warp to 1F East...")
        mgba.press_buttons(["Up"])
        time.sleep(2.0)
        print("New position after warp UP:", mgba.get_coordinates())
        exit(0)

# If pos is not (8, 11) and state_a_open is False, then we are in State B!
# Let's handle State B if we are still at (12, 11)
if pos == {"x": 12, "y": 11}:
    print("Mansion is in State B! (Row 11 gate is closed).")
    # Walk UP to Row 5
    steps = []
    for y in range(10, 4, -1):
        steps.append(("Up", {"x": 12, "y": y}))
    # Walk Left along Row 5 (it should be open in State B)
    for x in range(11, 0, -1):
        steps.append(("Left", {"x": x, "y": 5}))
    if run_steps(steps):
        print("Successfully reached B1F West NORTH in State B!")
        # Standing at (1, 5) facing UP, pick up the Secret Key!
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        print("Retrieving the Secret Key...")
        mgba.press_buttons([
            "A", "sleep 2500",
            "A", "sleep 2500",
            "A", "sleep 2500",
            "A", "sleep 2500"
        ])
        time.sleep(10.5)
        print("Final position:", mgba.get_coordinates())
        exit(0)
    else:
        print("Failed to walk LEFT to B1F West NORTH")
        exit(1)

print("Script finished.")
