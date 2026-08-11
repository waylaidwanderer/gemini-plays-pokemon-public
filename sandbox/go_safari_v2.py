import time
import bridge

print("Starting go_safari_v2.py...")

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

# First, dismiss the "Got away safely!" text
print("Dismissing battle text...")
bridge.press_buttons(["A"])
time.sleep(1.5)

pos = bridge.get_coordinates()
print(f"Current coordinates inside Area 1 (East): {pos}")
if pos is not None:
    # 1. Walk from (24, 16) to Area 2 (North) transition
    # Left 4 to (20, 16), Up 11 to (20, 5), Left 20 to (0, 5), Left 1 to transition
    area1_to_area2_from_east = (
        ["Left"] * 4 +
        ["Up"] * 11 +
        ["Left"] * 21
    )
    
    # 2. Area 2 (North) to Area 3 (West)
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
    
    # We will execute the first leg (Area 1 to Area 2)
    print("Navigating Area 1 (East) to Area 2 (North)...")
    walk_safely(area1_to_area2_from_east)
    
    pos = bridge.get_coordinates()
    print(f"Current coordinates: {pos}")
    
    # Execute the second leg (Area 2 to Area 3)
    print("Navigating Area 2 (North)...")
    walk_safely(area2_to_area3)
    
    pos = bridge.get_coordinates()
    print(f"Current coordinates inside Area 3 (West): {pos}")
else:
    print("Failed to get coordinates after battle.")
