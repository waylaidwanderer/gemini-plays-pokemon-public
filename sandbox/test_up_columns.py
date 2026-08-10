import bridge
import time

# Systematically test walking UP on each column from Column 1 to Column 13 along Row 14
curr = bridge.get_coordinates()
print(f"Starting systematic UP test from {curr}")

# First walk DOWN to Row 14
bridge.press_buttons(["Down", "sleep 300", "Down", "sleep 300"])
curr = bridge.get_coordinates()
print(f"Coordinates on Row 14: {curr}")

# We will test Column 10, then 9, 8, 7, 6, 5, 4, 3, 2, 1
for col in range(10, 0, -1):
    # Walk to (col, 14)
    curr = bridge.get_coordinates()
    while curr[0] != col:
        direction = "Left" if col < curr[0] else "Right"
        bridge.press_buttons([direction, "sleep 300"])
        new_curr = bridge.get_coordinates()
        if new_curr == curr:
            # Try to run away if stuck in battle
            # On BALL x30, press Down, Right, A to run
            bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1500"])
            bridge.press_buttons(["B", "sleep 200", "B", "sleep 200"])
            new_curr = bridge.get_coordinates()
        curr = new_curr
        
    # Now try to walk UP from (col, 14)
    print(f"Testing Column {col} at {curr}...")
    temp_curr = curr
    can_go_up = False
    for step in range(1, 6):
        bridge.press_buttons(["Up", "sleep 300"])
        new_curr = bridge.get_coordinates()
        if new_curr == temp_curr:
            break
        else:
            print(f"  Successfully moved UP to {new_curr}")
            temp_curr = new_curr
            can_go_up = True
            # If we reached row 9, we succeeded!
            if new_curr[1] <= 9:
                print(f"SUCCESS! Found a path UP Column {col} to {new_curr}!")
                break
                
    if can_go_up and temp_curr[1] <= 9:
        break
    else:
        # Walk back down to Row 14 if we moved but didn't reach row 9
        curr = bridge.get_coordinates()
        while curr[1] != 14:
            bridge.press_buttons(["Down", "sleep 300"])
            new_curr = bridge.get_coordinates()
            if new_curr == curr:
                # Escape battle
                bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1500"])
                bridge.press_buttons(["B", "sleep 200", "B", "sleep 200"])
                new_curr = bridge.get_coordinates()
            curr = new_curr

print(f"Test finished. Current position: {bridge.get_coordinates()}")
