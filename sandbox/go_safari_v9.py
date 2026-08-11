import time
import bridge

print("Starting go_safari_v9.py...")

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
print(f"Current coordinates: {pos}")

# Clean route to Area 3 (West) from (6, 24)
plateau_route = (
    ["Up"] +         # To (6, 23)
    ["Right"] * 16 + # To (22, 23)
    ["Up"] +         # To (22, 22) (climb onto plateau)
    ["Left"] * 6 +   # To (16, 22)
    ["Down"] * 5 +   # To (16, 27) (descend off plateau)
    ["Left"] * 4 +   # To (12, 27)
    ["Down"] * 5 +   # To (12, 32)
    ["Left"] * 4 +   # To (8, 32)
    ["Down"] * 3 +   # To (8, 35)
    ["Left"] * 2     # Transition to Area 3 (West) at (26, 0)
)

print("Navigating via Plateau to Area 3 (West)...")
walk_safely(plateau_route)

pos = bridge.get_coordinates()
print(f"Final coordinates inside Area 3 (West): {pos}")
