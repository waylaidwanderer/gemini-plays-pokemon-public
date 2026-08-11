import time
import bridge

print("Starting go_safari_v7.py...")

# Dismiss the "Got away safely!" text box
print("Dismissing text box...")
bridge.press_buttons(["B"])
time.sleep(1.0)

def handle_battle():
    print("Wild battle detected! Attempting to escape...")
    # Press B several times to clear any text
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.4)
    
    # Run is Down-Right-A in battle menu
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

# Walk to Area 3 (West) from (20, 23)
remaining_route = (
    ["Left"] * 4 + # To (16, 23)
    ["Down"] * 5 + # To (16, 28)
    ["Left"] * 4 + # To (12, 28)
    ["Down"] * 5 + # To (12, 33)
    ["Left"] * 4 + # To (8, 33)
    ["Down"] * 2 + # To (8, 35)
    ["Left"] * 2   # Transition to Area 3 (West) at (26, 0)
)

print("Navigating remaining route to Area 3 (West)...")
walk_safely(remaining_route)

pos = bridge.get_coordinates()
print(f"Final coordinates: {pos}")
