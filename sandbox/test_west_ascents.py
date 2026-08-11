import bridge
import time

print("Starting systematic western ascent search...")

# Verify position is (1, 32)
pos = bridge.get_coordinates()
print(f"Current position: {pos}")
if pos != (1, 32):
    print("Error: Not at (1, 32)")
    exit(1)

# 2. Test columns 3 to 8
for col in [3, 4, 5, 6, 7, 8]:
    pos = bridge.get_coordinates()
    if pos is None:
        continue
    cx, cy = pos
    print(f"At {cx}, {cy}. Heading to column {col} on Row 32...")
    
    # Walk to column 'col' on Row 32
    steps = col - cx
    if steps > 0:
        bridge.press_buttons(["Right"] * steps)
    elif steps < 0:
        bridge.press_buttons(["Left"] * abs(steps))
    time.sleep(0.5)
    
    # Verify we are at (col, 32)
    pos = bridge.get_coordinates()
    if pos != (col, 32):
        print(f"Failed to reach ({col}, 32), currently at {pos}")
        continue
        
    # Press UP to see if we can walk UP to Row 31
    print(f"Testing UP from ({col}, 32)...")
    bridge.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Check if we successfully moved UP
    new_pos = bridge.get_coordinates()
    if new_pos is not None and new_pos[1] == 31:
        print(f"!!! SUCCESS !!! FOUND GAP UP ON COLUMN {col} !!!")
        # Walk up to Row 28
        print("Walking up to Row 28...")
        bridge.press_buttons(["Up", "Up", "Up"])
        time.sleep(0.5)
        
        # Walk Right to Column 19
        pos = bridge.get_coordinates()
        if pos is not None:
            cx, cy = pos
            steps_right = 19 - cx
            print(f"Walking Right {steps_right} steps to Column 19 on Row 28...")
            bridge.press_buttons(["Right"] * steps_right)
            time.sleep(0.5)
            
            # Enter Pokémon Center (Up 1)
            print("Entering Pokémon Center...")
            bridge.press_buttons(["Up"])
            time.sleep(2.0)
            
            final_pos = bridge.get_coordinates()
            print(f"Final position inside Pokémon Center: {final_pos}")
        break
    else:
        print(f"Column {col} is blocked going UP (bumped on Row 31)")
