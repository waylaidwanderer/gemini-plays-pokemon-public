import mgba
import time

def test_mansion_switch_and_gate():
    pos = mgba.get_coordinates()
    print(f"Current position: {pos}")
    
    # 1. Walk to (2, 12) facing Up
    # We are at (1, 10). Path to (2, 12): Down, Down, Right, Up
    steps = ["Down", "Down", "Right", "Up"]
    for step in steps:
        mgba.press_buttons([step])
        time.sleep(0.3)
    
    print(f"At switch standing position: {mgba.get_coordinates()}")
    
    # Take screenshot before toggle
    img_before = mgba.take_screenshot()
    print("Screenshot before toggle taken.")
    
    # 2. Toggle the switch at (2, 11) with proper sleeps to avoid race conditions
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    print("Switch toggle sequence completed.")
    
    # Take screenshot after toggle
    img_after = mgba.take_screenshot()
    print("Screenshot after toggle taken.")
    
    # 3. Walk to (1, 10) and attempt to walk through the gate at (1, 9)
    # Path: Left, Up, Up
    steps_to_gate = ["Left", "Up", "Up"]
    for step in steps_to_gate:
        mgba.press_buttons([step])
        time.sleep(0.3)
    
    print(f"Standing at (1, 10): {mgba.get_coordinates()}")
    
    # Try to walk UP through the gate 3 times
    print("Attempting to walk through gate at (1, 9)...")
    for _ in range(3):
        mgba.press_buttons(["Up"])
        time.sleep(0.3)
        
    final_pos = mgba.get_coordinates()
    print(f"Final position after gate test: {final_pos}")

test_mansion_switch_and_gate()
