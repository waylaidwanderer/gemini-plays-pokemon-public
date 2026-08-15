import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    pos = get_pos()
    print(f"Starting buy_ticket_and_enter from: {pos}")
    
    # We are at (18, 4) in Fuchsia City. Walk UP to enter Gatehouse.
    if pos == (18, 4):
        print("Entering Safari Zone Gatehouse...")
        bridge.press_buttons(["Up", "sleep 1000"])
        time.sleep(1.0)
        
    pos = get_pos()
    print(f"Position inside Gatehouse: {pos}")
    
    # We should be at (3, 5) or similar inside the Gatehouse.
    # Walk to (3, 2) where the clerk is.
    while pos is not None and pos[1] > 2:
        print(f"Walking UP from {pos}")
        bridge.press_buttons(["Up", "sleep 450"])
        pos = get_pos()
        
    if pos is not None and pos[1] == 2:
        # Talk to the clerk at (3, 2) or face UP
        print("Interacting with Safari clerk...")
        bridge.press_buttons(["Up", "sleep 300"]) # face UP
        bridge.press_buttons(["A", "sleep 800"])  # Talk
        
        # Pay 500 and buy ticket
        print("Buying ticket...")
        for _ in range(5):
            bridge.press_buttons(["A", "sleep 800"])
            
        print("Dismissing any remaining dialogue...")
        for _ in range(3):
            bridge.press_buttons(["B", "sleep 400"])
            
        time.sleep(1.5)
        print(f"Position after entering Safari Zone: {bridge.get_coordinates()}")

if __name__ == "__main__":
    main()
