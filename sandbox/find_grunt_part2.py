import mgba
import time

def get_stable_coords():
    pos1 = mgba.get_coordinates()
    time.sleep(0.1)
    pos2 = mgba.get_coordinates()
    while pos1 != pos2:
        pos1 = pos2
        time.sleep(0.1)
        pos2 = mgba.get_coordinates()
    return pos1

# Start at (5, 1) inside Celadon Game Corner
pos = get_stable_coords()
print(f"Starting position: {pos}")

# 1. Walk Left to (3, 1)
while pos['x'] > 3:
    mgba.press_buttons(["Left"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"At (3, 1): {pos}. Walking Down to Row 7...")

# 2. Walk Down to Row 7
while pos['y'] < 7:
    mgba.press_buttons(["Down"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"At (3, 7): {pos}. Walking Right to Column 7...")

# 3. Walk Right to Column 7
while pos['x'] < 7:
    mgba.press_buttons(["Right"])
    time.sleep(0.35)
    pos = get_stable_coords()

print(f"At (7, 7): {pos}. Walking Up to Row 3...")

# 4. Walk Up to Row 3
# Note: (7, 2) is blocked by an NPC, so we stop at Row 3.
while pos['y'] > 3:
    # Check if there is a wandering NPC blocking us
    pos_before = get_stable_coords()
    mgba.press_buttons(["Up"])
    time.sleep(0.35)
    pos_after = get_stable_coords()
    if pos_after == pos_before:
        # Bypassing wandering NPC if blocked
        print("Blocked going Up. Trying Right then Up...")
        mgba.press_buttons(["Right", "Up", "Left"])
        time.sleep(1.0)
        pos_after = get_stable_coords()
    pos = pos_after

print(f"At (7, 3): {pos}. Walking Right to Column 14 to find Grunt...")

# 5. Walk Right to explore the room
# We want to go Right along Row 3 to find the Rocket Grunt
for step in range(15):
    pos_before = get_stable_coords()
    mgba.press_buttons(["Right"])
    time.sleep(0.35)
    pos_after = get_stable_coords()
    
    if pos_after == pos_before:
        print(f"Blocked going Right at: {pos_after}")
        scr = mgba.take_screenshot()
        print(f"Blockage screenshot saved at: {scr}")
        break
    
    pos = pos_after
    print(f"Walked Right to: {pos}")
    
    if step % 3 == 0:
        scr = mgba.take_screenshot()
        print(f"Screenshot at {pos} saved at: {scr}")

print("End of find_grunt_part2 script.")
