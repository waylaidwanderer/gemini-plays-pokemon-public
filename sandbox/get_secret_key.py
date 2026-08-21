import mgba
import time

def solve_b1f_mansion():
    print("Executing ultimate B1F route to retrieve the Secret Key...")
    
    # We are currently at (10, 1) in State A
    # 1. Walk Down Column 10 to (10, 11)
    for step in range(1, 11):
        mgba.press_buttons(["Down"])
        time.sleep(0.5)
    print(f"At Row 11: {mgba.get_coordinates()}")
    
    # 2. Walk Left to (3, 11)
    for _ in range(7):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
    print(f"At (3, 11): {mgba.get_coordinates()}")
    
    # 3. Walk to (1, 11) via Row 12 to bypass the statue
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    mgba.press_buttons(["Left", "Left"])
    time.sleep(1.0)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print(f"At (1, 11): {mgba.get_coordinates()}")
    
    # 4. Turn Right and toggle switch to State B
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    print("Facing Mewtwo statue. Toggling switch to State B...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Clear dialogue if any
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    print(f"Switch toggled! Position: {mgba.get_coordinates()}")
    
    # Now the switch is in State B!
    # 5. Walk to (5, 13) via Row 13
    mgba.press_buttons(["Down", "Down"])
    time.sleep(1.0)
    print(f"At (1, 13) in State B: {mgba.get_coordinates()}")
    for _ in range(4):
        mgba.press_buttons(["Right"])
        time.sleep(0.5)
    print(f"At (5, 13) in State B: {mgba.get_coordinates()}")
    
    # 6. Walk UP Column 5 to (5, 8)
    for step in range(1, 6):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
    print(f"At Column 5 Row 8: {mgba.get_coordinates()}")
    
    # 7. Walk Left to (4, 8)
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    print(f"At (4, 8): {mgba.get_coordinates()}")
    
    # 8. Walk UP Column 4 to (4, 5) (through open gates (4,7) and (4,6)!)
    for _ in range(3):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
    print(f"At (4, 5) in North section: {mgba.get_coordinates()}")
    
    # 9. Walk Left to (1, 5)
    for _ in range(3):
        mgba.press_buttons(["Left"])
        time.sleep(0.5)
    print(f"At (1, 5): {mgba.get_coordinates()}")
    
    # 10. Walk Up to (1, 4) (Secret Key!)
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    print(f"At Secret Key tile (1, 4): {mgba.get_coordinates()}")
    
    # 11. Face UP and retrieve Secret Key
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Clear dialogue
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    print(f"Retrieval complete! Final position: {mgba.get_coordinates()}")
    scr = mgba.take_screenshot()
    print(f"Final screenshot: {scr}")

solve_b1f_mansion()
