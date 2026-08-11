import time
import bridge

print("Starting go_safari_v3.py...")

def handle_battle():
    print("Wild battle detected! Attempting to escape...")
    # Escape sequence: Down, Right, A (to select RUN)
    # Clear any text boxes first with B
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

# Verify start position (26, 13)
pos = bridge.get_coordinates()
print(f"Current coordinates inside Area 1 (East): {pos}")
if pos != (26, 13):
    print("Warning: Not starting at (26, 13)!")

# 1. Walk from (26, 13) to Area 2 (North) transition
# Up 8 to (26, 5), Left 27 to transition to Area 2 (North) at (39, 31)
area1_to_area2 = (
    ["Up"] * 8 +
    ["Left"] * 27
)

# 2. Area 2 (North) to Area 3 (West)
area2_to_area3 = (
    ["Left"] * 17 +
    ["Up"] * 9 + # Walk to (22, 22)
    ["Left"] * 6 +
    ["Down"] * 5 + # Descend Western Southern Plateau to (16, 27)
    ["Left"] * 4 +
    ["Down"] * 5 +
    ["Left"] * 4 +
    ["Down"] * 3 +
    ["Left"] * 2 # Transition to Area 3 (West)
)

print("Navigating Area 1 (East) to Area 2 (North)...")
walk_safely(area1_to_area2)

pos = bridge.get_coordinates()
print(f"Current coordinates: {pos} (should be (39, 31) in Area 2)")

print("Navigating Area 2 (North)...")
walk_safely(area2_to_area3)

pos = bridge.get_coordinates()
print(f"Final coordinates inside Area 3 (West): {pos}")
