import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def buy_drink_roof_perfect():
    print("Starting from:", get_pos())
    
    # 1. We are currently at (17, 2). Walk left 1 step to (16, 2)
    press_and_wait("Left")
    print("At (16, 2):", get_pos())
    
    # 2. Go UP 4 floors to the Roof
    # Floor UP transition 1 (Even -> Odd)
    print("Floor UP 1...")
    press_and_wait("Up", 1.0)
    print("Current position:", get_pos())
    
    # Floor UP transition 2 (Odd -> Even)
    print("Floor UP 2...")
    for _ in range(4):
        press_and_wait("Left")
    press_and_wait("Up", 1.0)
    print("Current position:", get_pos())
    
    # Floor UP transition 3 (Even -> Odd)
    print("Floor UP 3...")
    for _ in range(4):
        press_and_wait("Right")
    press_and_wait("Up", 1.0)
    print("Current position:", get_pos())
    
    # Floor UP transition 4 (Odd -> Roof)
    print("Floor UP 4...")
    for _ in range(4):
        press_and_wait("Left")
    press_and_wait("Up", 1.0)
    print("Current position:", get_pos())
    
    # Now we should be on the Roof!
    # Let's walk to the vending machine
    print("--- Navigating on Roof ---")
    # Walk DOWN 1 step to Row 3 (just in case we are at 15, 2)
    press_and_wait("Down")
    
    # Walk Left 9 steps to Column 6
    for _ in range(9):
        press_and_wait("Left")
    print("At Column 6 on Row 3:", get_pos())
    
    # Walk UP 1 step to Row 2 (to face the vending machine at 6, 1)
    press_and_wait("Up")
    print("Facing vending machine at:", get_pos())
    
    # Interact with the vending machine
    print("Pressing A...")
    press_and_wait("A", 1.0)
    
    # Select Option 1 (Fresh Water)
    print("Selecting Fresh Water (Option 1)...")
    press_and_wait("A", 0.5)
    
    # Confirm Fresh Water dialogue
    print("Confirming dialogue 1...")
    press_and_wait("A", 1.0)
    print("Confirming dialogue 2...")
    press_and_wait("A", 1.0)
    
    # Interact again to buy Soda Pop (just in case)
    print("Interacting again...")
    press_and_wait("A", 1.0)
    print("Selecting Soda Pop (Option 2)...")
    press_and_wait("Down", 0.3)
    press_and_wait("A", 0.5)
    print("Confirming Soda Pop dialogue...")
    press_and_wait("A", 1.0)
    press_and_wait("A", 1.0)
    
    # Exit vending machine
    print("Exiting...")
    press_and_wait("B", 0.5)
    
    # Take screenshot of final state
    mgba.take_screenshot()
    print("Fresh Water and Soda Pop purchased successfully!")

buy_drink_roof_perfect()
