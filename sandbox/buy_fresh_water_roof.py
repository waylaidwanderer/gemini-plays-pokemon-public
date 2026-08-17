import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def climb_to_roof_and_buy():
    print("Starting from:", get_pos())
    
    # 1. Close text box (B)
    print("Closing text box...")
    press_and_wait("B", 0.5)
    
    # 2. Walk Right 3 steps to (17, 2) on 1F
    print("Moving to 1F UP escalator...")
    for _ in range(3):
        press_and_wait("Right")
    print("At 1F escalator:", get_pos())
    
    # 3. 1F -> 2F
    print("Warping 1F -> 2F...")
    press_and_wait("Up", 1.0)
    print("At 2F:", get_pos())
    
    # 4. 2F -> 3F
    print("Warping 2F -> 3F...")
    press_and_wait("Up", 1.0)
    print("At 3F:", get_pos())
    
    # 5. 3F -> 4F
    print("Warping 3F -> 4F...")
    press_and_wait("Up", 1.0)
    print("At 4F:", get_pos())
    
    # 6. 4F -> 5F
    print("Warping 4F -> 5F...")
    press_and_wait("Up", 1.0)
    print("At 5F:", get_pos())
    
    # 7. On 5F, walk Left 5 steps to (12, 2)
    print("Moving to 5F stairs...")
    for _ in range(5):
        press_and_wait("Left")
    print("At 5F stairs:", get_pos())
    
    # 8. 5F -> Roof
    print("Warping 5F -> Roof...")
    press_and_wait("Up", 1.0)
    print("At Roof:", get_pos())
    
    # 9. Walk DOWN 1 step to Row 3 (just in case we are at 15, 2)
    press_and_wait("Down")
    
    # 10. Walk Left 9 steps to Column 6
    for _ in range(9):
        press_and_wait("Left")
    print("At Column 6 Row 3 on Roof:", get_pos())
    
    # 11. Walk UP to face vending machine
    press_and_wait("Up")
    print("Facing vending machine at:", get_pos())
    
    # 12. Interact and buy Fresh Water
    print("Pressing A...")
    press_and_wait("A", 1.0)
    print("Selecting Fresh Water (Option 1)...")
    press_and_wait("A", 0.5)
    print("Confirming dialogue 1...")
    press_and_wait("A", 1.0)
    print("Confirming dialogue 2...")
    press_and_wait("A", 1.0)
    
    # 13. Interact again and buy Soda Pop
    print("Interacting again...")
    press_and_wait("A", 1.0)
    print("Selecting Soda Pop (Option 2)...")
    press_and_wait("Down", 0.3)
    press_and_wait("A", 0.5)
    print("Confirming Soda Pop dialogue...")
    press_and_wait("A", 1.0)
    press_and_wait("A", 1.0)
    
    # 14. Exit
    print("Exiting...")
    press_and_wait("B", 0.5)
    
    # Take screenshot of final state
    mgba.take_screenshot()
    print("Vending machine purchase completed successfully!")

climb_to_roof_and_buy()
