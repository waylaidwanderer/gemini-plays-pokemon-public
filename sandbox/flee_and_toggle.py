import mgba
import time

def flee_battle():
    print("Fleeing battle...")
    # Press B a few times to dismiss the encounter screen and transition to fight menu
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.4)
    
    # Press Down, Right, A to choose RUN
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(2.0) # Wait for text/escape animation
    
    # Press B a few times to dismiss "Escaped safely!" or similar text
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.4)

def toggle_switch():
    print("Initiating switch toggle...")
    # Ensure we are facing Left (the switch is at (2, 5) from (3, 5))
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    
    # 4 A-Press sequence with generous delays (2.0s)
    # A-Press 1: Interacts with the statue
    print("A-Press 1")
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    
    # A-Press 2: Advances text to YES/NO menu
    print("A-Press 2")
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    
    # A-Press 3: Selects YES (default)
    print("A-Press 3")
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    
    # A-Press 4: Dismisses the textbox and restores the overworld
    print("A-Press 4")
    mgba.press_buttons(["A"])
    time.sleep(2.0)

# 1. Flee the battle
flee_battle()

# Check position
pos = mgba.get_coordinates()
print(f"Position after fleeing: {pos}")

# 2. Toggle switch if we are at (3, 5)
if pos['x'] == 3 and pos['y'] == 5:
    toggle_switch()
    mgba.take_screenshot()
    pos_after = mgba.get_coordinates()
    print(f"Final Position: {pos_after}")
else:
    print("Not at (3, 5)! Maybe fleeing failed.")
    mgba.take_screenshot()
