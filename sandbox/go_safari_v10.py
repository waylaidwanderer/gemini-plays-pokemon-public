import time
import bridge

print("Starting go_safari_v10.py...")

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

# Safe path from (15, 25) in Center to Area 1 (East) at (29, 11)
center_to_area1_path = (
    ["Up"] * 2 +     # To (15, 23)
    ["Right"] * 14 + # To (29, 23)
    ["Up"] * 12 +    # To (29, 11)
    ["Right"] * 2    # Transition to Area 1 (East)
)

print("Navigating Safari Zone Center to Area 1 (East)...")
walk_safely(center_to_area1_path)

pos = bridge.get_coordinates()
print(f"Final coordinates inside Area 1 (East): {pos}")
