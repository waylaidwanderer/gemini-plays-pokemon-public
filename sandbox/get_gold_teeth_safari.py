import bridge
import time
import os
from PIL import Image

def escape_battle():
    print("Encountered a battle! Attempting to escape...")
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    bridge.press_buttons(["Down", "Right", "A"])
    time.sleep(1.2)
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.1)
    print("Escape sequence complete.")

def walk_to_waypoint(target_x, target_y):
    print(f"Navigating to waypoint ({target_x}, {target_y})...")
    stuck_count = 0
    last_coords = None
    
    while True:
        curr = bridge.get_coordinates()
        if curr is None:
            print("Coordinates are None. Waiting...")
            time.sleep(0.5)
            continue
            
        x, y = curr
        if x == target_x and y == target_y:
            print(f"Reached waypoint ({target_x}, {target_y})")
            return True
            
        if curr == last_coords:
            stuck_count += 1
            if stuck_count > 4:
                print(f"Stuck at {curr} trying to reach ({target_x}, {target_y}). Attempting escape...")
                escape_battle()
                stuck_count = 0
                time.sleep(0.5)
                # Press B to recover any open menus
                bridge.press_buttons(["B", "B"])
                time.sleep(0.5)
        else:
            stuck_count = 0
            last_coords = curr
            
        # Choose direction to move
        if x < target_x:
            btn = "Right"
        elif x > target_x:
            btn = "Left"
        elif y < target_y:
            btn = "Down"
        elif y > target_y:
            btn = "Up"
            
        bridge.press_buttons([btn])
        time.sleep(0.44)

# ==========================================================
# PHASE 0: Fuchsia City - CUT Bush and Walk to (26, 9)
# ==========================================================
print("Walking to (26, 14)...")
walk_to_waypoint(26, 14)

print("Opening Start menu...")
bridge.press_buttons(["Start"])
time.sleep(1.0)

print("Resetting Start menu cursor to POKEDEX...")
for _ in range(7):
    bridge.press_buttons(["Up"])
    time.sleep(0.1)

print("Selecting POKEMON...")
bridge.press_buttons(["Down", "A"])
time.sleep(1.0)

print("Resetting POKEMON cursor to first Pokémon...")
for _ in range(5):
    bridge.press_buttons(["Up"])
    time.sleep(0.1)

print("Selecting TRUFFLE...")
bridge.press_buttons(["Down", "A"])
time.sleep(1.0)

# Take screenshot of the submenu
scr = bridge.send_request("/api/take_screenshot") # Mid-script screenshot
screenshot_path = scr.get("screenshot_path")
if not screenshot_path:
    # Use mgba fallback if bridge request didn't return path
    import mgba
    screenshot_path = mgba.take_screenshot()

print("Analyzing submenu screenshot:", screenshot_path)
img = Image.open(screenshot_path)
gray = img.convert('L')
width, height = gray.size

scale_x = width / 160.0
scale_y = height / 144.0

cursor_x = int(83 * scale_x)
found_y = None

# Find the vertical coordinate of the black cursor arrow
for y in range(int(10 * scale_y), int(120 * scale_y)):
    val = gray.getpixel((cursor_x, y))
    if val < 50: # Black cursor pixel found
        found_y = y / scale_y
        break

if found_y is None:
    print("Could not find cursor arrow! Defaulting to index 0.")
    current_index = 0
else:
    print(f"Cursor arrow found at GBC y={found_y:.1f}")
    if found_y < 26:
        current_index = 0 # DIG
    elif found_y < 42:
        current_index = 1 # CUT
    elif found_y < 58:
        current_index = 2 # STATS
    elif found_y < 74:
        current_index = 3 # SWITCH
    else:
        current_index = 4 # CANCEL

print(f"Current selected option index: {current_index}")
downs_needed = (1 - current_index) % 5
print(f"Downs needed to reach CUT (index 1): {downs_needed}")

# Move to CUT
for _ in range(downs_needed):
    bridge.press_buttons(["Down"])
    time.sleep(0.3)

# Use CUT
print("Using CUT...")
bridge.press_buttons(["A"])
time.sleep(2.0) # Wait for animation

# Clear the dialogue box "TRUFFLE used CUT!"
print("Pressing A to clear dialogue...")
bridge.press_buttons(["A"])
time.sleep(1.0)

# Walk past the cut bush to (26, 9)
print("Walking UP to (26, 9)...")
walk_to_waypoint(26, 9)

print("Phase 0 Completed successfully! Position:", bridge.get_coordinates())
