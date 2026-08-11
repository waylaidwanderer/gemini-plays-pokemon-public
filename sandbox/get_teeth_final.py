import time
import bridge

print("Starting get_teeth_final.py...")

def handle_battle():
    print("Wild battle detected! Attempting to escape...")
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.4)
    
    bridge.press_buttons(["Down", "sleep 250", "Right", "sleep 250", "A"])
    time.sleep(3.5) # Wait for escape animation
    
    # Dismiss "Got away safely!"
    bridge.press_buttons(["B"])
    time.sleep(1.0)

def walk_safely(buttons_sequence):
    idx = 0
    while idx < len(buttons_sequence):
        # Battle check
        pos = bridge.get_coordinates()
        if pos is None:
            handle_battle()
            pos = bridge.get_coordinates()
            if pos is None:
                time.sleep(1.0)
                pos = bridge.get_coordinates()
                if pos is None:
                    print("Coordinates still None, escaping again...")
                    handle_battle()
                    pos = bridge.get_coordinates()
            continue
        
        btn = buttons_sequence[idx]
        print(f"Step {idx+1}/{len(buttons_sequence)}: Pressing {btn} at {pos}")
        bridge.press_buttons([btn])
        time.sleep(0.7)
        idx += 1

# Check current coordinates
pos = bridge.get_coordinates()
print(f"Current coordinates on plateau: {pos}")

# 1. Walk across plateau to (21, 16) - 15 Right
# 2. Descend East Stairs to (21, 18) - 2 Down
# 3. Walk Down Column 21 to (21, 24) - 6 Down
# 4. Walk Left to (19, 24) - 2 Left
route_to_teeth = (
    ["Right"] * 15 +
    ["Down"] * 2 +
    ["Down"] * 6 +
    ["Left"] * 2
)

print("Walking across plateau and down column 21 to (19, 24)...")
walk_safely(route_to_teeth)

# Turn down and pick up teeth
print("Facing down and picking up GOLD TEETH...")
bridge.press_buttons(["Down", "sleep 500", "A", "sleep 1000", "B", "sleep 500", "B"])

pos = bridge.get_coordinates()
print(f"Final coordinates: {pos}")
