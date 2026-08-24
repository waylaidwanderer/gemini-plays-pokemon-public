import mgba
import sys
import time
from PIL import Image

def get_pos():
    return mgba.get_coordinates()

def run_from_battle():
    print("Wild battle detected! Waiting 4.5 seconds for intro...")
    time.sleep(4.5)
    print("Dismissing text...")
    mgba.press_buttons(["B", "sleep 350", "B", "sleep 350", "B", "sleep 350"])
    time.sleep(0.5)
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "sleep 350", "Right", "sleep 350", "A", "sleep 1800"])
    print("Clearing escape text...")
    mgba.press_buttons(["B", "sleep 350", "B", "sleep 350", "B", "sleep 350"])
    time.sleep(1.0)
    print("Escape sequence complete.")

def walk_step(direction):
    pos_before = get_pos()
    mgba.press_buttons([direction, "sleep 450"])
    pos_after = get_pos()
    
    if pos_before == pos_after:
        time.sleep(0.3)
        sc = mgba.take_screenshot()
        img = Image.open(sc)
        pixel = img.getpixel((240, 360))
        if pixel[0] > 240 and pixel[1] > 240 and pixel[2] > 240:
            print("Confirmed wild battle! Running...")
            run_from_battle()
            mgba.press_buttons([direction, "sleep 450"])
            pos_after = get_pos()
        else:
            print(f"BUMPED going {direction} at {pos_before}!")
            
    return pos_before, pos_after

def walk_to(target_x, target_y):
    print(f"Walking to ({target_x}, {target_y})...")
    max_steps = 40
    steps = 0
    while steps < max_steps:
        pos = get_pos()
        x, y = pos['x'], pos['y']
        if x == target_x and y == target_y:
            print(f"Arrived at ({target_x}, {target_y})!")
            return True
        if x < target_x: direction = "Right"
        elif x > target_x: direction = "Left"
        elif y < target_y: direction = "Down"
        elif y > target_y: direction = "Up"
        pos_before, pos_after = walk_step(direction)
        if pos_before == pos_after:
            print(f"Failed step at {pos_before} going {direction}")
            return False
        steps += 1
    return False

# Self-recovering Phase Detection based on coordinates
pos = get_pos()
x, y = pos['x'], pos['y']

print("--- Pokémon Mansion Secret Key Self-Recovering Master Script ---")
print(f"Current Position: ({x}, {y})")

# Determine floor/map
# Since Cinnabar Island and Pokémon Mansion share some x,y values, we can look at specific values.
# On Cinnabar Island, y >= 12 (most of island) or y=3, etc.
# But inside 1F West, y goes up to 27.
# We can distinguish by y:
# Outside: y >= 12 on Cinnabar Island. Wait, Cinnabar Island y=12 is where we start.
# Inside 1F West: y is up to 27 (lands at (5, 27)).
# Inside 2F West: y=11, x=7, etc.
# Inside 3F West: x <= 12, y <= 12.

if y == 12 and x == 11:
    print("PHASE: Outside on Cinnabar Island. Walking to enter the Mansion...")
    # Walk Right to (18, 12)
    if not walk_to(18, 12): sys.exit(1)
    # Walk Up to (18, 5)
    if not walk_to(18, 5): sys.exit(1)
    # Walk Left to (6, 5)
    if not walk_to(6, 5): sys.exit(1)
    # Walk Up to (6, 3)
    if not walk_to(6, 3): sys.exit(1)
    # Enters door
    print("Entering Mansion...")
    mgba.press_buttons(["Up", "sleep 1500"])
    pos = get_pos()
    print("Inside Mansion 1F West! Position:", pos)
    sys.exit(0)

elif y == 27 and x == 5:
    print("PHASE: Inside Mansion 1F West (landing). Walking to 2F West stairs...")
    if not walk_to(5, 11): sys.exit(1)
    if not walk_to(8, 11): sys.exit(1)
    if not walk_to(8, 10): sys.exit(1)
    if not walk_to(5, 10): sys.exit(1)
    print("Warping UP to 2F West...")
    mgba.press_buttons(["Left", "sleep 1500"])
    pos = get_pos()
    print("Inside 2F West! Position:", pos)
    sys.exit(0)

elif y == 11 and x == 5:
    print("PHASE: Inside 2F West (landing). Walking to 3F West stairs...")
    if not walk_to(7, 11): sys.exit(1)
    print("Warping UP to 3F West...")
    mgba.press_buttons(["Up", "sleep 1500"])
    pos = get_pos()
    print("Inside 3F West! Position:", pos)
    sys.exit(0)

elif y == 11 and x == 7:
    print("PHASE: Inside 3F West (landing). Walking to switch at (2, 12)...")
    if not walk_to(3, 11): sys.exit(1)
    if not walk_to(3, 12): sys.exit(1)
    if not walk_to(2, 12): sys.exit(1)
    print("Face UP towards statue switch...")
    mgba.press_buttons(["Up", "sleep 450"])
    print("Toggling switch to State B...")
    mgba.press_buttons(["A", "sleep 1200"]) # A secret switch!
    mgba.press_buttons(["A", "sleep 1200"]) # Press it? YES
    mgba.press_buttons(["A", "sleep 1200"]) # Who wouldn't?
    mgba.press_buttons(["A", "sleep 1200"]) # Close dialogue
    print("Switch toggled successfully! Position:", get_pos())
    sys.exit(0)

elif y == 12 and x == 2:
    print("PHASE: At 3F West switch in State B. Walking and crossing to 3F East...")
    if not walk_to(1, 12): sys.exit(1)
    if not walk_to(1, 8): sys.exit(1)
    if not walk_to(12, 8): sys.exit(1)
    if not walk_to(12, 6): sys.exit(1)
    if not walk_to(26, 6): sys.exit(1)
    print("Dropped through pitfall! Waiting 2.0 seconds...")
    time.sleep(2.0)
    print("Position after drop (1F East fenced room):", get_pos())
    sys.exit(0)

elif y == 4 and x == 26:
    print("PHASE: Dropped onto 1F East inside fenced room. Walking to B1F stairs...")
    if not walk_to(26, 3): sys.exit(1)
    if not walk_to(22, 3): sys.exit(1)
    print("Stepping onto B1F stairs...")
    mgba.press_buttons(["Up", "sleep 2000"]) # warps to B1F East (22, 3)
    print("Warped down to B1F! Position:", get_pos())
    sys.exit(0)

elif (y == 3 or y == 2) and x == 22:
    print("PHASE: On B1F East. Walking along B1F Row 5 directly to B1F West...")
    if not walk_to(22, 5): sys.exit(1)
    if not walk_to(21, 5): sys.exit(1)
    if not walk_to(1, 5): sys.exit(1)
    print("Facing UP towards Secret Key...")
    mgba.press_buttons(["Up", "sleep 450"])
    print("Retrieving Secret Key...")
    mgba.press_buttons(["A", "sleep 1200"]) # Obtained dialogue
    mgba.press_buttons(["A", "sleep 1200"]) # Clear dialogue
    print("SECRET KEY RETRIEVED SUCCESSFULLY! Digging out...")
    
    # Use DIG
    mgba.press_buttons(["Start", "sleep 800"])
    mgba.press_buttons(["Down", "sleep 400", "A", "sleep 1200"]) # Select PKMN
    for _ in range(5):
        mgba.press_buttons(["Down", "sleep 300"])
    mgba.press_buttons(["A", "sleep 1000"]) # Select TRUFFLE
    mgba.press_buttons(["A", "sleep 3500"]) # Select DIG
    print("DIG used! Position:", get_pos())
    sys.exit(0)

else:
    print(f"Unknown phase at coordinate: ({x}, {y}). Running generic recovery walk back to Cinnabar Island...")
    # Just in case we got lost or stuck
    # Let's use DIG to recover to Cinnabar Island!
    mgba.press_buttons(["Start", "sleep 800"])
    mgba.press_buttons(["Down", "sleep 400", "A", "sleep 1200"]) # Select PKMN
    for _ in range(5):
        mgba.press_buttons(["Down", "sleep 300"])
    mgba.press_buttons(["A", "sleep 1000"]) # Select TRUFFLE
    mgba.press_buttons(["A", "sleep 3500"]) # Select DIG
    print("DIG used for recovery! Position:", get_pos())
    sys.exit(0)
