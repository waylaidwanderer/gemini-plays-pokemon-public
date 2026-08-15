import time
import sys
import os

# Add current path to import bridge
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Mashing through clerk dialog to buy ticket...")
    
    # Loop until we warp to Safari Zone Center at (15, 25)
    attempts = 0
    while attempts < 35:
        pos = get_pos()
        if pos == (15, 25):
            print("Successfully warped into Safari Zone Center!")
            return True
            
        print(f"Current pos: {pos}. Pressing A and B...")
        bridge.press_buttons(["A", "sleep 300", "B", "sleep 200"])
        attempts += 1
        time.sleep(0.1)
        
    print("Failed to warp after 35 attempts.")
    return False

if __name__ == "__main__":
    main()
