import bridge
import time

print("Starting systematic descent search v2...")

# 1. Walk UP to Row 18
print("Moving UP to Row 18...")
bridge.press_buttons(["Up", "Up", "Up"])
time.sleep(0.5)

# 2. Walk LEFT to Column 24
print("Moving LEFT to Column 24...")
bridge.press_buttons(["Left"] * 11)
time.sleep(0.5)

# 3. Walk DOWN to Row 21
print("Moving DOWN to Row 21...")
bridge.press_buttons(["Down", "Down", "Down"])
time.sleep(0.5)

# 4. Test columns from 23 down to 3
for col in range(23, 2, -1):
    current = bridge.get_coordinates()
    if current is None:
        continue
    cx, cy = current
    print(f"At {cx}, {cy}. Heading to column {col} on Row 21...")
    
    # Walk to column 'col'
    steps = cx - col
    if steps > 0:
        bridge.press_buttons(["Left"] * steps)
    elif steps < 0:
        bridge.press_buttons(["Right"] * abs(steps))
    time.sleep(0.5)
    
    # Verify we are at (col, 21)
    current = bridge.get_coordinates()
    if current != (col, 21):
        print(f"Failed to reach ({col}, 21), currently at {current}")
        continue
        
    # Press DOWN to see if we can descend to Row 22
    bridge.press_buttons(["Down"])
    time.sleep(0.5)
    
    # Check if we successfully moved DOWN
    new_pos = bridge.get_coordinates()
    if new_pos is not None and new_pos[1] == 22:
        print(f"!!! SUCCESS !!! FOUND ENTRANCE DOWN ON COLUMN {col} !!!")
        break
    else:
        print(f"Column {col} is blocked (bumped on Row 22)")
