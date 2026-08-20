import mgba
import time

def test_interact():
    print("Testing interaction around (7, 11)...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Let's turn LEFT and press A to see if the NPC at (6, 11) talks
    print("Facing Left and pressing A...")
    mgba.press_buttons(["Left", "A"])
    time.sleep(1.0)
    mgba.take_screenshot()
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Let's turn UP and press A to see if there's an NPC at (7, 10)
    print("Facing Up and pressing A...")
    mgba.press_buttons(["Up", "A"])
    time.sleep(1.0)
    mgba.take_screenshot()
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Try walking Down to (7, 12)
    print("Trying to walk Down...")
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    pos = mgba.get_coordinates()
    print("Position after walking Down:", pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    test_interact()
