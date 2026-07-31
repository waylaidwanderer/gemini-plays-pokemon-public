import mgba
import time

def wait_for_movement():
    p1 = mgba.get_coordinates()
    time.sleep(0.12)
    p2 = mgba.get_coordinates()
    while p1 != p2:
        p1 = p2
        time.sleep(0.12)
        p2 = mgba.get_coordinates()
    return p1

# We start at (15, 18)
print("Start Position:", mgba.get_coordinates())

# First, let's go back to (16, 13) stopper:
# Walk Left to (14, 18) -> Up onto (14, 17) -> spins to (14, 15) -> walk Right to (16, 15) -> Up onto (16, 14) -> spins to (16, 13)
mgba.press_buttons(["Left"])
wait_for_movement()
mgba.press_buttons(["Up"])
wait_for_movement() # spins to (14, 15)
mgba.press_buttons(["Right", "Right", "Up"])
wait_for_movement() # spins to (16, 13)
pos = mgba.get_coordinates()
print("At (16, 13) stopper:", pos)

# Let's map out the grid of coordinates in the eastern room:
# Columns 18 to 22, Rows 11 to 15
# We will step on each and check if we warp!

# Define a systematic grid path:
# Starting at (16, 13), we walk Right to (18, 13)
mgba.press_buttons(["Right", "Right"])
pos = wait_for_movement()
print("At (18, 13):", pos)

# We will test all candidate cells around column 18, 19, 20, 21, 22 on rows 11, 12, 13, 14, 15
# If we warp, the script will exit or detect a coordinate change
start_map_pos = pos

candidates = [
    # Walk to (19, 13)
    "Right",
    # Test (19, 12)
    "Up", "Down",
    # Test (19, 11)
    "Up", "Up", "Down", "Down",
    # Walk to (20, 13) (defeat grunt or fight him)
    "Right",
    # Test (21, 13)
    "Right",
    # Test (22, 13)
    "Right",
    # Let's go Down column 22
    "Down", # (22, 14)
    "Down", # (22, 15)
    # Test column 21
    "Left", # (21, 15)
    "Up",   # (21, 14)
    "Down", # (21, 15)
    # Test column 20
    "Left", # (20, 15)
    "Up",   # (20, 14)
    "Down", # (20, 15)
    # Test column 19
    "Left", # (19, 15)
    "Up",   # (19, 14)
    "Down"  # (19, 15)
]

for i, btn in enumerate(candidates):
    print(f"Pressing {btn}...")
    mgba.press_buttons([btn])
    pos = wait_for_movement()
    print(f"Position: {pos}")
    # Check if we transitioned to a different map (B4F)
    # On B4F, coordinates are usually different or we are on a different floor structure
    # Let's check if the position changed significantly or if we warped
    # (If we warped, we would land on B4F or B2F)
    # Let's check if pos['y'] is very different or we are not on B3F
    # Let's print out if we detect warp
    if pos == {'x': 18, 'y': 13} and btn == "Up":
        # we know (18, 14) is blocked
        pass

# Take screenshot at the end
screenshot_path = mgba.take_screenshot()
print(f"Final Screenshot: {screenshot_path}")

