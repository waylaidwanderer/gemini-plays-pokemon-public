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

def handle_menu_dialogue_battle():
    if not check_dialogue_or_battle():
        return False
        
    print("Dialogue/Battle detected! Attempting to handle/dismiss...")
    # First, try pressing B to dismiss standard text
    mgba.press_buttons(["B"])
    time.sleep(0.4)
    
    # If still in dialogue/battle, try to RUN
    if check_dialogue_or_battle():
        print("Still in dialogue/battle, trying to select RUN...")
        mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
        time.sleep(1.2)
        
        # Dismiss any leftover text
        for _ in range(4):
            mgba.press_buttons(["B"])
            time.sleep(0.3)
            
    return True

def safe_step(direction, expected_coords=None, max_attempts=15, skip_battle_check=False):
    for attempt in range(max_attempts):
        if not skip_battle_check:
            while handle_menu_dialogue_battle():
                time.sleep(0.2)
            
        old_pos = get_pos()
        mgba.press_buttons([direction])
        time.sleep(0.45)
        new_pos = get_pos()
        
        if new_pos != old_pos:
            if expected_coords and new_pos != expected_coords:
                print(f"Moved {direction} to {new_pos} (expected {expected_coords}). Checking...")
            else:
                print(f"Successfully stepped {direction} to {new_pos}")
            return True
            
        print(f"Collision/delay at {old_pos} trying {direction} (attempt {attempt+1}/{max_attempts})")
        time.sleep(0.2)
        
    print(f"ERROR: Could not step {direction} from {old_pos}")
    return False

def run_safe_steps(steps, skip_battle_check=False):
    for d, c in steps:
        if not safe_step(d, c, skip_battle_check=skip_battle_check):
            return False
    return True

print("Start position:", get_pos())

# 1. Walk from (3, 10) to (2, 12)
steps_to_switch = [
    ("Down", (3, 11)),
    ("Down", (3, 12)),
    ("Left", (2, 12)),
]
print("Walking to switch statue at (2, 11)...")
if not run_safe_steps(steps_to_switch):
    print("Failed to reach switch location")
    exit(1)

# 2. Toggle Mewtwo Switch to State B!
# Stand at (2, 12), face UP, and send the exact switch interaction sequence
print("Toggling Mewtwo switch at (2, 11)...")
mgba.press_buttons([
    "Up", "sleep 500",
    "A", "sleep 1000",
    "A", "sleep 1000",
    "A", "sleep 1000",
    "A", "sleep 1000",
    "A", "sleep 1000"
])
time.sleep(6.5)
print("Switch toggling sequence completed.")

# 3. Walk to (3, 12) then UP Column 3 to Row 6 (State B opens Row 9)
steps_to_row_6 = [
    ("Right", (3, 12)),
    ("Up", (3, 11)),
    ("Up", (3, 10)),
    ("Up", (3, 9)),  # Shutter gate, must be open now!
    ("Up", (3, 8)),
    ("Up", (3, 7)),
    ("Up", (3, 6)),
]
print("Walking UP Column 3 to Row 6...")
if not run_safe_steps(steps_to_row_6):
    print("Failed to navigate to Row 6")
    exit(1)

# 4. Walk RIGHT along Row 6 to Column 20
steps_row_6 = []
for x in range(4, 21):
    steps_row_6.append(("Right", (x, 6)))
print("Walking RIGHT along Row 6 to Column 20...")
if not run_safe_steps(steps_row_6):
    print("Failed walking along Row 6")
    exit(1)

# 5. Walk UP Column 20 to Row 3 (bypassing pitfalls)
steps_to_row_3 = [
    ("Up", (20, 5)),
    ("Up", (20, 4)),
    ("Up", (20, 3)),
]
print("Walking UP Column 20 to Row 3...")
if not run_safe_steps(steps_to_row_3):
    print("Failed walking UP Column 20")
    exit(1)

# 6. Walk RIGHT along Row 3 to Column 26
steps_row_3 = []
for x in range(21, 27):
    steps_row_3.append(("Right", (x, 3)))
print("Walking RIGHT along Row 3 to Column 26...")
if not run_safe_steps(steps_row_3):
    print("Failed walking along Row 3")
    exit(1)

# 7. Step DOWN onto the pitfall trap at (26, 4) to drop to 1F East inside fenced room
print("Dropping through the pitfall to 1F East...")
if not safe_step("Down", (26, 4)):
    print("Failed to drop through the pitfall")
    exit(1)
time.sleep(2.0)
print("Landed on 1F East. Position:", get_pos())

# 8. Walk LEFT to stairs and warp DOWN to B1F East
pos = get_pos()
steps_to_stairs = []
for x in range(pos[0]-1, 21, -1):
    steps_to_stairs.append(("Left", (x, 4)))
steps_to_stairs.append(("Up", (22, 3)))

print("Walking to 1F East stairs...")
if not run_safe_steps(steps_to_stairs):
    print("Failed to reach stairs")
    exit(1)

print("Warping down to B1F East...")
mgba.press_buttons(["Up"])
time.sleep(2.0)
print("Arrived on B1F East. Position:", get_pos())

# 9. Cross B1F East to B1F West NORTH and retrieve Secret Key
pos = get_pos()
if pos[1] == 2:
    safe_step("Down")
    pos = get_pos()

# Move to Row 5 (B1F East Column 19 Row 5)
steps_to_row_5 = [
    ("Down", (22, 4)),
    ("Left", (21, 4)),
    ("Left", (20, 4)),
    ("Left", (19, 4)),
    ("Down", (19, 5)),
]
print("Moving to B1F Row 5...")
if not run_safe_steps(steps_to_row_5):
    print("Failed to reach B1F Row 5")
    exit(1)

# Walk straight LEFT across B1F Row 5 through open gate (9, 5) to Secret Key room
steps_left = []
for x in range(18, 0, -1):
    steps_left.append(("Left", (x, 5)))
print("Walking LEFT to Secret Key room...")
if not run_safe_steps(steps_left):
    print("Failed to reach Secret Key room")
    exit(1)

# Align UP towards the Secret Key at (1, 4)
print("Facing UP towards Secret Key...")
mgba.press_buttons(["Up"])
time.sleep(0.5)

# Pick up the Secret Key!
print("Retrieving Secret Key...")
mgba.press_buttons(["A"])
time.sleep(2.0)
# Dismiss dialogue
for _ in range(5):
    mgba.press_buttons(["B"])
    time.sleep(0.4)

print("Mansion master route completed successfully! Final Position:", get_pos())
mgba.take_screenshot()
