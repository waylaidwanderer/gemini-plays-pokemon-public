import time
import bridge

print("Starting go_safari_v8.py...")

def handle_battle():
    print("Wild battle detected! Attempting to escape...")
    # Escape sequence: Down, Right, A (to select RUN)
    # Clear any text boxes first with B
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

# Check coordinates
pos = bridge.get_coordinates()
print(f"Current coordinates: {pos}")

# Walk from (8, 24) to Area 3 (West) via gate at (7, 25)
shortcut_route = (
    ["Left"] +       # To (7, 24)
    ["Down"] * 2 +   # To (7, 26) through gate
    ["Right"] +      # To (8, 26)
    ["Down"] * 9 +   # To (8, 35)
    ["Left"] * 2     # Transition to Area 3 (West)
)

print("Navigating shortcut to Area 3 (West)...")
walk_safely(shortcut_route)

pos = bridge.get_coordinates()
print(f"Final coordinates inside Area 3 (West): {pos}")
