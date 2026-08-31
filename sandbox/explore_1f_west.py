import mgba
import time

def check_text():
    # Close any open dialogue or start menu
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    # Check if a text box is on screen by taking a screenshot or checking coordinates
    # We can just check coordinates
    pos = mgba.get_coordinates()
    return pos

def walk_and_interact(path, face_dir):
    # Close start menu
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    print(f"Walking to interact position...")
    for step in path:
        mgba.press_buttons([step])
        time.sleep(0.4)
        
    print(f"Facing {face_dir}...")
    mgba.press_buttons([face_dir])
    time.sleep(0.4)
    
    print("Pressing A...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Check if dialogue opened by checking if we can move or if coordinates changed
    # Actually, let's take a screenshot to see if a textbox appeared!
    screenshot = mgba.take_screenshot()
    print("Screenshot saved after A-press:", screenshot)
    
    # Clear dialogue if any opened
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def main():
    # Currently at (3, 7) on 1F West
    # We want to check the central yellow/brown block (Columns 6-7, Rows 4-5)
    # Let's check it from the bottom:
    # 1. Walk to (6, 6) and face UP (interact with (6, 5))
    # Path: Right to (5, 7), Up to (5, 6), Right to (6, 6)
    # Wait, (4, 7) is open in State A!
    # So we can walk: Right to (4, 7), Right to (5, 7), Up to (5, 6), Right to (6, 6)
    print("--- Test 1: (6, 6) face UP ---")
    walk_and_interact(["Right", "Right", "Up", "Right"], "Up")
    
    # 2. Walk to (7, 6) and face UP (interact with (7, 5))
    # Path from (6, 6): Right to (7, 6)
    print("--- Test 2: (7, 6) face UP ---")
    walk_and_interact(["Right"], "Up")
    
    # 3. Walk to (8, 5) and face LEFT (interact with (7, 5))
    # Path from (7, 6): Right to (8, 6), Up to (8, 5)
    print("--- Test 3: (8, 5) face LEFT ---")
    walk_and_interact(["Right", "Up"], "Left")
    
    # 4. Walk to (5, 5) and face RIGHT (interact with (6, 5))
    # Path from (8, 5): Down to (8, 6), Left to (5, 6), Up to (5, 5)
    print("--- Test 4: (5, 5) face RIGHT ---")
    walk_and_interact(["Down", "Left", "Left", "Left", "Up"], "Right")

if __name__ == "__main__":
    main()
