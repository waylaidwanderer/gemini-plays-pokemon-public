import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def check_dialogue_or_battle():
    # Robust white-only check to completely eliminate dark tile false positives on B1F
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    white_pixels = 0
    total_pixels = 0
    for y in range(112, 144):
        for x in range(8, 152):
            r, g, b = img_std.getpixel((x, y))[:3]
            total_pixels += 1
            if r > 220 and g > 220 and b > 220:
                white_pixels += 1
                
    ratio = white_pixels / total_pixels
    return ratio > 0.80

def run_from_battle():
    print("Dismissing battle intro text...")
    for i in range(12):
        mgba.press_buttons(["B"])
        time.sleep(0.35)
        
    print("Attempting to select RUN...")
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
    time.sleep(2.0)
    
    print("Dismissing escape dialogue...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.35)

def safe_step(direction, expected_coords=None, max_attempts=15):
    for attempt in range(max_attempts):
        if check_dialogue_or_battle():
            print("Dialogue/Battle detected. Handling...")
            run_from_battle()
            time.sleep(0.5)
            continue
            
        old_pos = get_pos()
        mgba.press_buttons([direction])
        time.sleep(0.55)
        new_pos = get_pos()
        
        if new_pos != old_pos:
            if expected_coords and new_pos != expected_coords:
                print(f"Moved {direction} to {new_pos} (expected {expected_coords}). Checking...")
            else:
                print(f"Successfully stepped {direction} to {new_pos}")
            return True
            
        print(f"Collision/delay at {old_pos} trying {direction} (attempt {attempt+1}/{max_attempts})")
        time.sleep(0.25)
        
    print(f"ERROR: Could not step {direction} from {old_pos}")
    return False

def run_safe_steps(steps):
    for d, c in steps:
        if not safe_step(d, c):
            return False
    return True

def go_to_switch():
    pos = get_pos()
    steps_to_switch = []
    if pos == (3, 10):
        steps_to_switch = [
            ("Down", (3, 11)),
            ("Down", (3, 12)),
            ("Left", (2, 12)),
        ]
    elif pos == (1, 10):
        steps_to_switch = [
            ("Down", (1, 11)),
            ("Down", (1, 12)),
            ("Right", (2, 12)),
        ]
    elif pos == (2, 12):
        pass
    else:
        print("Warning: unexpected start position", pos)
        # fallback to walk to Row 12, then Column 2, then Up
        while pos[1] < 12:
            pos = step("Down")
        while pos[0] < 2:
            pos = step("Right")
        while pos[0] > 2:
            pos = step("Left")
        while pos[1] > 12:
            pos = step("Up")
            
    if steps_to_switch:
        print("Walking to switch standing position...")
        if not run_safe_steps(steps_to_switch):
            return False
            
    print("Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    return True

def step(direction):
    old_pos = get_pos()
    mgba.press_buttons([direction])
    time.sleep(0.55)
    return get_pos()

def toggle_switch_once():
    print("Toggling Mewtwo Switch with exactly 4 slow A-presses...")
    mgba.press_buttons([
        "A", "sleep 1500",
        "A", "sleep 1500",
        "A", "sleep 1500",
        "A", "sleep 1500"
    ])
    time.sleep(7.0)
    print("Switch toggle complete!")

def test_gate_open():
    print("Walking to Column 1 Row 10 to test...")
    # Walk to (1, 12)
    if not safe_step("Left", (1, 12)):
        return False
    # Walk Up Column 1
    if not safe_step("Up", (1, 11)):
        return False
    if not safe_step("Up", (1, 10)):
        return False
        
    # Try to step UP to (1, 9)
    old_pos = get_pos()
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    new_pos = get_pos()
    
    if new_pos == (1, 9):
        print("Column 1 Row 9 gate is OPEN!")
        # Continue the rest of the 3F West path
        steps_up = [
            ("Up", (1, 8)),
            ("Up", (1, 7)),
            ("Up", (1, 6)),
        ]
        if not run_safe_steps(steps_up):
            return False
        return True
    else:
        print("Column 1 Row 9 gate is CLOSED.")
        return False

# Master loop:
# We are currently at some position. Go to switch, toggle, and test.
# If closed, toggle again and test.

print("Starting Master Verification Protocol...")

# State 1: Try current state or toggle once
if not go_to_switch():
    print("Failed to reach switch")
    exit(1)

toggle_switch_once()

if test_gate_open():
    print("SUCCESS! Column 1 Row 9 gate is OPEN. Continuing the route...")
    
    # 5. Walk RIGHT along Row 6 to Column 20
    print("Walking RIGHT along Row 6 to Column 20...")
    pos = get_pos()
    while pos[0] < 20:
        pos = step("Right")
        
    # 6. Walk UP Column 20 to Row 3
    print("Walking UP Column 20 to Row 3...")
    while get_pos()[1] > 3:
        step("Up")
        
    # 7. Walk RIGHT along Row 3 to Column 26
    print("Walking RIGHT along Row 3 to Column 26...")
    while get_pos()[0] < 26:
        step("Right")
        
    # 8. Drop through the pitfall to 1F East inside the fenced room
    print("Dropping through the pitfall to 1F East...")
    step("Down")
    time.sleep(2.5)
    pos = get_pos()
    print("Landed on 1F East inside fenced room:", pos)
    
    # 9. Walk to B1F East stairs and warp down
    if pos[1] == 4:
        step("Down")
    pos = get_pos()
    while pos[0] > 22:
        pos = step("Left")
    while pos[1] > 3:
        pos = step("Up")
        
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = get_pos()
    print("Position on B1F East:", pos)
    
    # 10. Cross B1F East to B1F West NORTH
    if pos[1] == 2:
        step("Down")
    # Walk to Column 21
    step("Left")
    # Down to Row 5
    step("Down")
    step("Down")
    # Left to Column 1
    pos = get_pos()
    while pos[0] > 1:
        pos = step("Left")
        
    # 11. Retrieve Secret Key!
    print("Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    print("Retrieving Secret Key...")
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
    print("Mansion fully solved! Secret Key retrieved successfully! Current Position:", get_pos())
    mgba.take_screenshot()
    exit(0)

# If we are here, the gate was CLOSED, meaning we toggled to the WRONG state.
# Let's walk back to switch and toggle again!
print("Gate was closed. Walking back to switch to toggle again...")
if not go_to_switch():
    print("Failed to reach switch on retry")
    exit(1)

toggle_switch_once()

if test_gate_open():
    print("SUCCESS on retry! Column 1 Row 9 gate is OPEN. Continuing the route...")
    
    # 5. Walk RIGHT along Row 6 to Column 20
    print("Walking RIGHT along Row 6 to Column 20...")
    pos = get_pos()
    while pos[0] < 20:
        pos = step("Right")
        
    # 6. Walk UP Column 20 to Row 3
    print("Walking UP Column 20 to Row 3...")
    while get_pos()[1] > 3:
        step("Up")
        
    # 7. Walk RIGHT along Row 3 to Column 26
    print("Walking RIGHT along Row 3 to Column 26...")
    while get_pos()[0] < 26:
        step("Right")
        
    # 8. Drop through the pitfall to 1F East inside the fenced room
    print("Dropping through the pitfall to 1F East...")
    step("Down")
    time.sleep(2.5)
    pos = get_pos()
    print("Landed on 1F East inside fenced room:", pos)
    
    # 9. Walk to B1F East stairs and warp down
    if pos[1] == 4:
        step("Down")
    pos = get_pos()
    while pos[0] > 22:
        pos = step("Left")
    while pos[1] > 3:
        pos = step("Up")
        
    print("Stepping UP to warp down to B1F East...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    pos = get_pos()
    print("Position on B1F East:", pos)
    
    # 10. Cross B1F East to B1F West NORTH
    if pos[1] == 2:
        step("Down")
    # Walk to Column 21
    step("Left")
    # Down to Row 5
    step("Down")
    step("Down")
    # Left to Column 1
    pos = get_pos()
    while pos[0] > 1:
        pos = step("Left")
        
    # 11. Retrieve Secret Key!
    print("Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    print("Retrieving Secret Key...")
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
    print("Mansion fully solved! Secret Key retrieved successfully! Current Position:", get_pos())
    mgba.take_screenshot()
    exit(0)
else:
    print("ERROR: Gate is still closed in BOTH switch states! Something is fundamentally wrong.")
    exit(1)
