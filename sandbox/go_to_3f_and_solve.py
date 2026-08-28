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
        time.sleep(0.3)
        
    print("Attempting to select RUN...")
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A"])
    time.sleep(2.0)
    
    print("Dismissing escape dialogue...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

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

# Starting at (5, 13) on 2F West (State A)
print("Starting definitive Mansion solution from current position (5, 13) on 2F West...")

# 1. Walk Up Column 5 and Right Row 11 to the stairs at (7, 11)
steps_to_stairs = [
    ("Up", (5, 12)),
    ("Up", (5, 11)),
    ("Right", (6, 11)),
    ("Right", (7, 11)),
]
for d, c in steps_to_stairs:
    if not safe_step(d, c):
        print("Failed to reach stairs")
        exit(1)
        
# 2. Step UP onto stairs at (7, 10) to warp UP to 3F West
print("Stepping UP to warp to 3F West...")
if not safe_step("Up"):
    print("Failed to warp UP to 3F West")
    exit(1)
time.sleep(1.5)
pos = get_pos()
print("Landed on 3F West at:", pos)

# 3. On 3F West, navigate to switch standing position (2, 12)
# Land coordinate on 3F West should be (7, 11).
# Walk to (2, 12) via Row 10 to avoid staircase warp:
# - Left to (6, 11)
# - Up to (6, 10)
# - Left to (5, 10)
# - Left to (4, 10)
# - Down to (4, 11) -> (4, 12) -> (4, 13)
# - Left to (3, 13) -> (2, 13)
# - Up to (2, 12)
steps_on_3f = [
    ("Left", (6, 11)),
    ("Up", (6, 10)),
    ("Left", (5, 10)),
    ("Left", (4, 10)),
    ("Down", (4, 11)),
    ("Down", (4, 12)),
    ("Down", (4, 13)),
    ("Left", (3, 13)),
    ("Left", (2, 13)),
    ("Up", (2, 12)),
]
print("Walking to switch standing position on 3F West...")
for d, c in steps_on_3f:
    if not safe_step(d, c):
        print("Failed navigating 3F West")
        exit(1)
        
# 4. Face UP and toggle the Mewtwo switch to State B
print("Facing UP...")
mgba.press_buttons(["Up"])
time.sleep(1.0)

print("Toggling switch to State B with exactly 4 slow A-presses...")
mgba.press_buttons([
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500",
    "A", "sleep 1500"
])
time.sleep(7.0)
print("Switch toggle complete! Player pushed to:", get_pos())

# 5. Walk Left on Row 13 to Column 1
if not safe_step("Left", (1, 13)):
    exit(1)
    
# 6. Walk Up Column 1 to Row 6 (crossing open gate at (1, 9))
for y in range(12, 5, -1):
    if not safe_step("Up", (1, y)):
        exit(1)
        
# 7. Walk Right along Row 6 to Column 20
for x in range(2, 21):
    if not safe_step("Right", (x, 6)):
        exit(1)
        
# 8. Walk Up Column 20 to Row 3
for y in range(5, 2, -1):
    if not safe_step("Up", (20, y)):
        exit(1)
        
# 9. Walk Right along Row 3 to Column 26
for x in range(21, 27):
    if not safe_step("Right", (x, 3)):
        exit(1)
        
# 10. Drop through pitfall to 1F East
print("Stepping Down to drop through the pitfall...")
if not safe_step("Down"):
    print("Failed to drop through pitfall")
    exit(1)
time.sleep(2.5)
pos = get_pos()
print("Landed on 1F East inside fenced room:", pos)

# 11. Step Down to (26, 5) or similar if needed to exit landing tile
if pos[1] == 4:
    if not safe_step("Down"):
        print("Failed to step Down from landing tile")
        exit(1)
        
# 12. Walk to Column 22 Row 2 and warp DOWN to B1F East
pos = get_pos()
while pos[0] > 22:
    if not safe_step("Left"):
        exit(1)
    pos = get_pos()
while pos[1] > 3:
    if not safe_step("Up"):
        exit(1)
    pos = get_pos()
    
print("Stepping UP to warp down to B1F East...")
mgba.press_buttons(["Up"])
time.sleep(2.0)
pos = get_pos()
print("Position on B1F East after warping:", pos)

# 13. Walk to Column 19 Row 5 via Row 4 to bypass Row 5 Column 20-21 closed gates
if pos[1] == 2:
    if not safe_step("Down"):
        exit(1)
if not safe_step("Left", (21, 3)):
    exit(1)
if not safe_step("Down", (21, 4)):
    exit(1)
# Walk Left on Row 4 to Column 19
for x in range(20, 18, -1):
    if not safe_step("Left", (x, 4)):
        exit(1)
# Down to Row 5
if not safe_step("Down", (19, 5)):
    exit(1)
    
# 14. Walk straight Left on Row 5 to Column 1 (Secret Key room)
for x in range(18, 0, -1):
    if not safe_step("Left", (x, 5)):
        exit(1)
        
# 15. Retrieve the Secret Key!
pos = get_pos()
if pos == (1, 5):
    print("Aligning UP towards the Secret Key...")
    mgba.press_buttons(["Up"])
    time.sleep(1.0)
    
    print("Retrieving Secret Key...")
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    # Dismiss dialogue
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        
    print("Mansion fully solved! Secret Key retrieved successfully! Current Position:", get_pos())
    mgba.take_screenshot()
