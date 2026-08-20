import mgba
import time

def toggle_and_menu():
    print("Moving Up from (2, 13) to (2, 12)...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # 1. Walk Up to (2, 12)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Position after Up:", pos)
    
    if pos['x'] != 2 or pos['y'] != 12:
        print("Failed to reach (2, 12)!")
        mgba.take_screenshot()
        return False
        
    # 2. Toggle switch to State B
    print("Toggling switch at (2, 11) to State B...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Press B to dismiss "Not quite yet!"
    print("Dismissing dialogue...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # 3. Open Start menu
    print("Opening Start menu...")
    mgba.press_buttons(["Start"])
    time.sleep(1.0)
    
    mgba.take_screenshot()
    return True

if __name__ == "__main__":
    toggle_and_menu()
