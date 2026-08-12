import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def enter_safari_safe():
    print("Starting safe dialog sequence to enter Safari Zone...")
    
    # 1. Start dialogue with clerk
    bridge.press_buttons(["A", "sleep 700"])
    
    # 2. Welcome to Safari Zone!
    bridge.press_buttons(["A", "sleep 700"])
    
    # 3. For just 500, you can catch...
    bridge.press_buttons(["A", "sleep 700"])
    
    # 4. Would you like to join? Select YES (defaults to YES, press A)
    bridge.press_buttons(["A", "sleep 700"])
    
    # 5. That'll be 500, thank you!
    bridge.press_buttons(["A", "sleep 700"])
    
    # 6. We only use special Safari Balls...
    # Receive 30 Safari Balls!
    bridge.press_buttons(["A", "sleep 700"])
    
    # 7. We'll call you when you run out of time or balls...
    bridge.press_buttons(["A", "sleep 700"])
    
    # 8. Have a great game! (Warps the player in!)
    bridge.press_buttons(["A", "sleep 2500"])
    
    print("Dialog sequence completed! Checking position...")
    pos = get_pos()
    print(f"Position: {pos}")
    return pos

if __name__ == "__main__":
    enter_safari_safe()
