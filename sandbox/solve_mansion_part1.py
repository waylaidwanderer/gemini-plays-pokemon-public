import mgba
import time
import os

# Cleanup extensionless notepads
extensionless_to_delete = [
    'notepads/Locations/FuchsiaGym',
    'notepads/Locations/SafariZone'
]
for path in extensionless_to_delete:
    if os.path.exists(path):
        try:
            os.remove(path)
            print(f"Deleted extensionless notepad: {path}")
        except Exception as e:
            print(f"Error deleting {path}: {e}")

# Update Progression_And_Party_Stats.md
stats_path = "notepads/Progression_And_Party_Stats.md"
if os.path.exists(stats_path):
    with open(stats_path, 'r') as f:
        content = f.read()
    obsolete = "- **SECRET KEY:** Located on B1F West at `(1, 4)`, currently retrieving it."
    if obsolete in content:
        content = content.replace(obsolete, "- **SECRET KEY:** Located on B1F West at `(1, 4)`, currently retrieving it.")
    # Ensure there is no mention of "but not yet retrieved because our Bag was full!"
    content = content.replace("but not yet retrieved because our Bag was full!", "")
    with open(stats_path, 'w') as f:
        f.write(content)
    print("Updated Progression_And_Party_Stats.md")

def handle_battle():
    print("Coordinates did not change. Likely a battle! Attempting to flee...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_step(tx, ty, direction):
    attempts = 0
    while attempts < 10:
        pos = mgba.get_coordinates()
        if pos['x'] == tx and pos['y'] == ty:
            return True
            
        mgba.press_buttons([direction])
        time.sleep(0.55)
        new_pos = mgba.get_coordinates()
        
        if new_pos == pos:
            print(f"Bumped at {pos} going {direction}. Attempting battle escape...")
            handle_battle()
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
        else:
            if new_pos['x'] == tx and new_pos['y'] == ty:
                return True
        attempts += 1
    return False

# --- PART 1: WALK OUTSIDE VIA COLUMN 17 TO MANSION AND TOGGLE SWITCH ON 2F WEST ---

pos = mgba.get_coordinates()
print("Starting definitive Mansion run Part 1 from Cinnabar outside:", pos)

if pos['x'] == 11 and pos['y'] == 12:
    path_enter = [
        (12, 12, 'Right'), # Move Right to Column 17 to bypass Poké Center
        (13, 12, 'Right'),
        (14, 12, 'Right'),
        (15, 12, 'Right'),
        (16, 12, 'Right'),
        (17, 12, 'Right'),
        (17, 11, 'Up'), # Walk UP Column 17 to Row 4
        (17, 10, 'Up'),
        (17, 9, 'Up'),
        (17, 8, 'Up'),
        (17, 7, 'Up'),
        (17, 6, 'Up'),
        (17, 5, 'Up'),
        (17, 4, 'Up'),
        (16, 4, 'Left'), # Walk LEFT Row 4 to Column 6
        (15, 4, 'Left'),
        (14, 4, 'Left'),
        (13, 4, 'Left'),
        (12, 4, 'Left'),
        (11, 4, 'Left'),
        (10, 4, 'Left'),
        (9, 4, 'Left'),
        (8, 4, 'Left'),
        (7, 4, 'Left'),
        (6, 4, 'Left'),
        (6, 3, 'Up'), # Enter Mansion
    ]
    print("Step 1: Entering the Mansion...")
    for target in path_enter:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to enter Mansion at ({tx}, {ty})")
            exit()
            
    time.sleep(2.0) # Wait for transition
    pos_inside = mgba.get_coordinates()
    print("Landed inside Mansion! Position:", pos_inside)
    
    # Walk UP immediately to clear exit warp at (5, 27)
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    mgba.press_buttons(["Up"])
    time.sleep(0.55)
    
# We are inside Mansion 1F West at (5, 23) in State A.
pos = mgba.get_coordinates()
if pos['x'] == 5 and pos['y'] == 23:
    path_to_stairs = [
        (7, 23, 'Right'),
        (7, 10, 'Down'),
    ]
    print("Step 2: Going UP the stairs to 2F West...")
    for target in path_to_stairs:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach 2F West stairs at ({tx}, {ty})")
            exit()
            
    time.sleep(2.0) # Wait for stairs transition

# We are on 2F West at (7, 10) in State A.
pos = mgba.get_coordinates()
if pos['x'] == 7 and pos['y'] == 10:
    path_to_switch = [
        (7, 11, 'Down'),
        (2, 11, 'Left'),
        (2, 12, 'Down'),
    ]
    print("Step 3: Walking to 2F West switch...")
    for target in path_to_switch:
        tx, ty, d = target
        if not walk_step(tx, ty, d):
            print(f"Failed to reach switch at ({tx}, {ty})")
            exit()
            
    print("At (2, 12). Facing UP and toggling switch to State B...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "B"])
    time.sleep(1.5)

print("End of Part 1! Current position:", mgba.get_coordinates())
mgba.take_screenshot()
