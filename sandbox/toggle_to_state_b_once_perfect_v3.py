import mgba
import time
from PIL import Image

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def check_dialogue_or_battle():
    scr_file = mgba.take_screenshot()
    img = Image.open(scr_file)
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    black_or_white = 0
    total_pixels = 0
    for y in range(112, 144):
        for x in range(8, 152):
            r, g, b = img_std.getpixel((x, y))[:3]
            total_pixels += 1
            is_bw = (r < 55 and g < 55 and b < 55) or (r > 200 and g > 200 and b > 200)
            if is_bw:
                black_or_white += 1
                
    ratio = black_or_white / total_pixels
    return ratio > 0.88

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
    if pos == (1, 10):
        steps_to_switch = [
            ("Down", (1, 11)),
            ("Down", (1, 12)),
            ("Right", (2, 12)),
        ]
    elif pos == (1, 12):
        steps_to_switch = [
            ("Right", (2, 12)),
        ]
    elif pos == (2, 12):
        pass
    else:
        # Fallback to walk to (2, 12) from elsewhere
        print("Warning: unexpected starting position", pos)
        
    if steps_to_switch:
        print("Walking to switch...")
        if not run_safe_steps(steps_to_switch):
            return False
            
    print("Facing UP...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    return True

def toggle_switch_once():
    print("Toggling switch with exactly 4 slow A-presses...")
    mgba.press_buttons([
        "A", "sleep 1500",
        "A", "sleep 1500",
        "A", "sleep 1500",
        "A", "sleep 1500"
    ])
    time.sleep(7.0)
    print("Switch toggle complete!")

def test_gate_open():
    print("Walking to gate to test...")
    # Walk Left to (1, 12)
    if not safe_step("Left", (1, 12)):
        return False
    # Walk Up to (1, 11)
    if not safe_step("Up", (1, 11)):
        return False
    # Walk Up to (1, 10)
    if not safe_step("Up", (1, 10)):
        return False
    # Walk Up to (1, 9) (the gate)
    # If the gate is open, this will succeed and we will be at (1, 9)
    old_pos = get_pos()
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    new_pos = get_pos()
    if new_pos == (1, 9):
        print("Gate is OPEN! Walking up to (1, 8)...")
        safe_step("Up", (1, 8))
        return True
    else:
        print("Gate is CLOSED!")
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
    print("SUCCESS! Mansion is in the correct state and we passed the gate!")
    exit(0)

# If we are here, the gate was CLOSED, meaning the previous state was B and we toggled to A,
# OR we need to toggle again. Let's walk back to switch and toggle again!
print("Gate was closed. Walking back to switch to toggle again...")
if not go_to_switch():
    print("Failed to reach switch on retry")
    exit(1)

toggle_switch_once()

if test_gate_open():
    print("SUCCESS on retry! Mansion is in the correct state and we passed the gate!")
    exit(0)
else:
    print("ERROR: Gate is still closed in BOTH switch states! Something is fundamentally wrong.")
    exit(1)
