import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def run_away():
    print("Interaction/Battle detected. Clearing...")
    for _ in range(4):
        bridge.press_buttons(["B", "sleep 250"])
    bridge.press_buttons(["Right", "sleep 250", "Down", "sleep 250", "A", "sleep 1200"])
    bridge.press_buttons(["B", "sleep 300"])

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 400"])

def test_east_plateau():
    # Currently at (28, 22).
    # 1. Walk to stairs at (24, 15) and climb
    # 2. Walk to row 12 and try to go Right
    # 3. Walk to row 13 and try to go Right
    # 4. Walk to row 14 and try to go Right
    
    # Walk to (24, 16)
    path_to_stairs = ["Left", "Left", "Left", "Left", "Up"]
    for direction in path_to_stairs:
        walk_step(direction)
        print(f"Current pos: {get_pos()}")
        
    # Walk Up to row 12
    for _ in range(3):
        walk_step("Up")
        print(f"Current pos: {get_pos()}")
        
    # We should be at (24, 12)
    # Walk Right to Column 26
    for _ in range(2):
        walk_step("Right")
        print(f"Current pos: {get_pos()}")
        
    # Now we are at (26, 12). Try to walk Right!
    print("Trying to walk Right from (26, 12) to (27, 12)...")
    walk_step("Right")
    print(f"Position after trying Right from (26, 12): {get_pos()}")
    
    # Try row 13
    print("Moving to row 13...")
    walk_step("Down")
    print(f"Current pos: {get_pos()}")
    print("Trying to walk Right from (26, 13) to (27, 13)...")
    walk_step("Right")
    print(f"Position after trying Right from (26, 13): {get_pos()}")
    
    # Try row 14
    print("Moving to row 14...")
    walk_step("Down")
    print(f"Current pos: {get_pos()}")
    print("Trying to walk Right from (26, 14) to (27, 14)...")
    walk_step("Right")
    print(f"Position after trying Right from (26, 14): {get_pos()}")

if __name__ == "__main__":
    test_east_plateau()
