import time
import bridge

print("Starting get_teeth.py...")

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

# 1. Walk from (15, 24) to plateau (6, 16)
route_to_plateau = (
    ["Left"] * 5 +   # To (10, 24)
    ["Up"] * 1 +     # To (10, 23)
    ["Left"] * 4 +   # To (6, 23)
    ["Up"] * 7       # To (6, 16) (climb West Stairs)
)

print("Walking to West Stairs and climbing to plateau...")
walk_safely(route_to_plateau)

pos = bridge.get_coordinates()
print(f"Final coordinates: {pos}")
