import mgba
import time

# We are at (1, 10). Let's scan the walkable tiles in x=1..3, y=10..16
# We will use simple walk steps and return to (1, 10) after each test.
# This will construct a complete map of the area!

# Coordinates to test
coords = []
for y in range(10, 17):
    for x in range(1, 4):
        coords.append({"x": x, "y": y})

walkable_tiles = []
solid_tiles = []

# Move to (1, 10)
mgba.press_buttons(["B"])
time.sleep(0.3)

print("Starting coordinate walkability scan...")
for target in coords:
    # First, always walk to (1, 10) (if we are not already there)
    curr = mgba.get_coordinates()
    # Since we only walk to neighboring tiles, let's use a simple pathfinder to go back to (1, 10)
    # We can always walk Down/Up/Right/Left to (1, 10) since we know the path is open.
    # Actually, from any tile in x=1..2, y=10..16, the path to (1, 10) is open along Column 1 or 2.
    # Let's just walk to (1, 10) step-by-step
    while curr != {"x": 1, "y": 10}:
        if curr["x"] > 1:
            mgba.press_buttons(["Left"])
            time.sleep(0.4)
        elif curr["y"] > 10:
            mgba.press_buttons(["Up"])
            time.sleep(0.4)
        elif curr["y"] < 10:
            mgba.press_buttons(["Down"])
            time.sleep(0.4)
        curr = mgba.get_coordinates()
        
    # Now we are at (1, 10). Let's try to walk to target.
    # To walk to target (x, y):
    # We can walk to (2, 10), then Down/Up to target y, then Right to target x.
    # Let's see if we can do this.
    success = True
    path = []
    # If target is (1, 10), it is walkable
    if target == {"x": 1, "y": 10}:
        walkable_tiles.append(target)
        continue
        
    # Build path to target via Column 2 (since Column 2 is open)
    # Walk Right to (2, 10)
    path.append(("Right", {"x": 2, "y": 10}))
    # Walk to y
    curr_y = 10
    while curr_y != target["y"]:
        d = "Down" if target["y"] > curr_y else "Up"
        curr_y += 1 if target["y"] > curr_y else -1
        path.append((d, {"x": 2, "y": curr_y}))
    # Walk to x
    if target["x"] != 2:
        d = "Right" if target["x"] > 2 else "Left"
        path.append((d, target))
        
    # Execute path
    for d, c in path:
        mgba.press_buttons([d])
        time.sleep(0.45)
        pos = mgba.get_coordinates()
        if pos != c:
            # Blocked!
            success = False
            break
            
    if success:
        walkable_tiles.append(target)
    else:
        solid_tiles.append(target)

print("Walkable tiles:")
print(walkable_tiles)
print("Solid tiles:")
print(solid_tiles)
