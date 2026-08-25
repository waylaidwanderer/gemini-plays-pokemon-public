import mgba
import time

def main():
    # We are at (1, 10)
    # Walk DOWN to (1, 12)
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    mgba.press_buttons(["Down"])
    time.sleep(0.4)
    # Walk RIGHT to (2, 12)
    mgba.press_buttons(["Right"])
    time.sleep(0.4)
    print("At:", mgba.get_coordinates())
    
    # Face UP
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Press A to open switch dialogue
    print("Opening switch dialogue...")
    mgba.press_buttons(["A"])
    time.sleep(1.8) # Wait for text to print completely!
    
    # Press A to select YES
    print("Selecting YES...")
    mgba.press_buttons(["A"])
    time.sleep(1.8) # Wait for "Pressed it!" to print completely!
    
    # Press A to dismiss "Pressed it!"
    print("Dismissing...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Dismiss any leftover text just in case
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    print("Toggled carefully! Position:", mgba.get_coordinates())

if __name__ == "__main__":
    main()
