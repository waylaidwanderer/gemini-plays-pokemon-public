import time
import bridge

print("Starting exit_center.py from inside...")

# Check current coordinates
pos = bridge.get_coordinates()
print(f"Current coordinates inside Pokémon Center: {pos}")

if pos is not None:
    # Walk Left to Column 3 on Row 5 (or current row if we can)
    # If we are on Row 4, let's walk Down to Row 5 first
    if pos[1] == 4:
        print("Walking DOWN to Row 5...")
        bridge.press_buttons(["Down"])
        time.sleep(0.6)
        pos = bridge.get_coordinates()
        
    if pos is not None:
        steps_left = pos[0] - 3
        print(f"Walking LEFT {steps_left} steps to Column 3...")
        for _ in range(steps_left):
            bridge.press_buttons(["Left"])
            time.sleep(0.6)
            
        pos = bridge.get_coordinates()
        print(f"Coordinates: {pos}")
        
        # Walk Down 3 steps to exit
        print("Walking DOWN to exit...")
        for _ in range(3):
            bridge.press_buttons(["Down"])
            time.sleep(0.6)
            
        # Give a little extra time for the transition
        time.sleep(1.5)
        
        pos = bridge.get_coordinates()
        print(f"Coordinates outside: {pos}")
else:
    print("Failed to get coordinates.")
