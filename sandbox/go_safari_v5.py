import time
import bridge

print("Starting go_safari_v5.py from current position...")

def handle_battle():
    print("Wild battle detected! Attempting to escape...")
    for _ in range(5):
        bridge.press_buttons(["B"])
        time.sleep(0.3)
    
    # Run is Down-Right-A in battle menu
    bridge.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A"])
    time.sleep(3.0) # Wait for escape animation

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
print(f"Current coordinates inside Area 2 (North): {pos}")

# Route to Area 3 (West) from (22, 19)
area2_to_area3 = (
    ["Down"] * 4 + # To (22, 23)
    ["Down"] * 1 + # To (22, 24) climbs onto plateau
    ["Left"] * 6 + # To (16, 24)
    ["Down"] * 4 + # To (16, 28) descends stairs
    ["Left"] * 4 + # To (12, 28)
    ["Down"] * 5 + # To (12, 33)
    ["Left"] * 4 + # To (8, 33)
    ["Down"] * 2 + # To (8, 35)
    ["Left"] * 2   # Transition to Area 3 (West) at (26, 0)
)

print("Navigating Area 2 (North) to Area 3 (West)...")
walk_safely(area2_to_area3)

pos = bridge.get_coordinates()
print(f"Coordinates after execution: {pos}")
