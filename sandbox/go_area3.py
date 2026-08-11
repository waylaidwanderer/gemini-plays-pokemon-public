import time
import bridge

print("Starting go_area3.py...")

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
print(f"Current coordinates inside Area 3 (West): {pos}")

# Walk down column 26 to row 14, then left through the gap to (23, 14)
route = (
    ["Down"] * 14 +
    ["Left"] * 3
)

print("Walking to (23, 14)...")
walk_safely(route)

pos = bridge.get_coordinates()
print(f"Final coordinates: {pos}")
