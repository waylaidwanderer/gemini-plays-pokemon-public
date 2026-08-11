import time
import bridge

print("Starting go_safari_v4.py from (22, 19)...")

def handle_battle():
    print("Wild battle detected! Attempting to escape...")
    for _ in range(3):
        bridge.press_buttons(["B"])
        time.sleep(0.3)
    
    bridge.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A"])
    time.sleep(2.5) # Wait for escape animation

def walk_safely(buttons_sequence):
    for idx, btn in enumerate(buttons_sequence):
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
        
        # Move
        print(f"Step {idx+1}/{len(buttons_sequence)}: Pressing {btn}")
        bridge.press_buttons([btn])
        time.sleep(0.6)

# Verify start position (22, 19)
pos = bridge.get_coordinates()
print(f"Current coordinates inside Area 2 (North): {pos}")
if pos != (22, 19):
    print("Warning: Not starting at (22, 19)!")

# Optimized route to Area 3 (West)
area2_to_area3_optimized = (
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

print("Navigating Area 2 (North)...")
walk_safely(area2_to_area3_optimized)

pos = bridge.get_coordinates()
print(f"Coordinates inside Area 3 (West): {pos}")
