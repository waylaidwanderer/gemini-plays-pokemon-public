import time
import bridge

print("Starting go_safari.py...")

def handle_battle():
    print("Wild battle detected! Attempting to escape...")
    # Escape sequence: Down, Right, A (to select RUN)
    # Let's also do a few B presses before to clear any entry text
    for _ in range(3):
        bridge.press_buttons(["B"])
        time.sleep(0.3)
    
    bridge.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A"])
    time.sleep(2.5) # Wait for escape animation

def walk_safely(buttons_sequence):
    for idx, btn in enumerate(buttons_sequence):
        # Check if in battle (get_coordinates returns None)
        pos = bridge.get_coordinates()
        if pos is None:
            # We are likely in a battle! Let's handle it
            handle_battle()
            # Try to get coordinates again
            pos = bridge.get_coordinates()
            if pos is None:
                # Still in battle or transition? Sleep and try again
                time.sleep(1.0)
                pos = bridge.get_coordinates()
                if pos is None:
                    print("Coordinates still None, trying to escape again...")
                    handle_battle()
                    pos = bridge.get_coordinates()
        
        # Press the movement button
        print(f"Step {idx+1}/{len(buttons_sequence)}: Pressing {btn}")
        bridge.press_buttons([btn])
        time.sleep(0.6)

# Main Navigation Sequence
# 1. Safari Zone Center to Area 1 (East)
center_to_area1 = (
    ["Up"] +
    ["Right"] * 14 +
    ["Up"] * 13 +
    ["Right"] # Transition to Area 1
)

# 2. Area 1 (East) to Area 2 (North)
area1_to_area2 = (
    ["Right"] * 20 +
    ["Up"] * 3 + # Climb Southern Plateau to (20, 20)
    ["Left"] * 8 +
    ["Down"] * 2 + # Descend stairs to (12, 22)
    ["Left"] * 3 +
    ["Up"] * 5 + # Walk to (9, 17)
    ["Right"] * 1 +
    ["Up"] * 5 + # Walk to (10, 12)
    ["Up"] * 5 +
    ["Right"] * 2 +
    ["Up"] * 1 + # Climb Northern Plateau to (12, 6)
    ["Right"] * 5 +
    ["Down"] * 2 + # Descend to (17, 8)
    ["Right"] * 3 +
    ["Up"] * 5 + # Walk UP to (20, 3) (bypassing row 4-6)
    ["Left"] * 13 + # Walk Left to Column 7
    ["Down"] * 2 + # Down to (7, 5)
    ["Left"] * 7 + # Transition to Area 2
    ["Left"] # Trigger transition warp
)

# 3. Area 2 (North) to Area 3 (West)
area2_to_area3 = (
    ["Left"] * 17 +
    ["Up"] * 8 + # Walk to (22, 23)
    ["Up"] * 1 +
    ["Left"] * 6 +
    ["Down"] * 5 + # Descend Western Southern Plateau to (16, 27)
    ["Left"] * 4 +
    ["Down"] * 5 +
    ["Left"] * 4 +
    ["Down"] * 3 +
    ["Left"] * 2 # Transition to Area 3 (West)
)

print("Navigating Safari Zone Center...")
walk_safely(center_to_area1)

print("Navigating Area 1 (East)...")
walk_safely(area1_to_area2)

print("Navigating Area 2 (North)...")
walk_safely(area2_to_area3)

print("Completed transitions! Checking coordinates...")
pos = bridge.get_coordinates()
print(f"Current coordinates inside Area 3 (West): {pos}")
