import mgba
import time

def flee_battle_safe():
    print("Fleeing battle...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.5)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    print("Finished fleeing.")

def main():
    # We are in battle, first flee
    flee_battle_safe()
    
    # We should be at (3, 11) in the overworld.
    # Turn left to face the Mewtwo statue at (2, 11)
    print("Turning Left to face switch...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    # Interact with switch (requires exactly 4 A-presses)
    print("Interacting with the switch to toggle to State A...")
    mgba.press_buttons(["A", "sleep 300", "A", "sleep 300", "A", "sleep 300", "A", "sleep 300"])
    time.sleep(1.0)
    
    scr = mgba.take_screenshot()
    print("Screenshot:", scr)
    print("Mansion should now be in State A!")

if __name__ == "__main__":
    main()
