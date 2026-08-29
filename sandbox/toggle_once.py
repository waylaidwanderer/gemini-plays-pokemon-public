import mgba
import time

def main():
    print("toggle_once: Walking to (2, 12)...")
    # We are at (1, 10)
    mgba.press_buttons(["Down", "sleep 500", "Down", "sleep 500", "Right", "sleep 500"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print(f"Position: {pos}")
    
    # Face Up
    mgba.press_buttons(["Up", "sleep 500"])
    time.sleep(1.0)
    
    # Toggle switch with single press_buttons sequence
    print("Sending toggle sequence with sleeps...")
    mgba.press_buttons(["A", "sleep 600", "A", "sleep 600", "A", "sleep 600", "A", "sleep 600"])
    time.sleep(3.0)
    
    # Walk Left to (1, 12)
    print("Walking Left...")
    mgba.press_buttons(["Left", "sleep 500"])
    time.sleep(1.0)
    
    # Walk Up to (1, 10)
    print("Walking Up...")
    mgba.press_buttons(["Up", "sleep 500", "Up", "sleep 500"])
    time.sleep(1.5)
    
    # Check if (1, 9) is now open by trying to step UP to (1, 9)
    print("Attempting to step UP to (1, 9)...")
    mgba.press_buttons(["Up", "sleep 500"])
    time.sleep(1.0)
    
    print(f"Final position: {mgba.get_coordinates()}")

if __name__ == "__main__":
    main()
