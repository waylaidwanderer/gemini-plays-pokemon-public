import mgba
import time

def main():
    print("Starting healing sequence with Nurse Joy...")
    
    # 1. Walk Up to (3, 4) from (3, 7)
    for _ in range(3):
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        
    pos = mgba.get_coordinates()
    print("Current position in front of counter:", pos)
    
    if pos == {'x': 3, 'y': 4}:
        print("Interacting with Nurse Joy...")
        # Press A to start talking
        mgba.press_buttons(["A"])
        time.sleep(1.0)
        
        # We need to spam A to advance dialogue and select YES
        # "Welcome to our Pokemon Center!" -> Press A
        # "Would you like me to heal..." -> Select YES (press A)
        # "Okay, I'll take your Pokemon..." -> Press A
        # (Heals Pokemon and plays jingle) -> Sleep 4 seconds
        # "Thank you for waiting!" -> Press A
        # "We hope to see you again!" -> Press A
        
        for i in range(3):
            mgba.press_buttons(["A"])
            time.sleep(1.0)
            
        print("Waiting for healing jingle...")
        time.sleep(4.5)
        
        for i in range(3):
            mgba.press_buttons(["A"])
            time.sleep(1.0)
            
        # Press B to make sure dialogue is completely closed
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        
        print("Healing complete! Taking screenshot...")
        mgba.take_screenshot()
    else:
        print("Failed to reach (3, 4)!")
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
