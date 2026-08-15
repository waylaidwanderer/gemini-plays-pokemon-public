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
    print("Closing BAG and exiting Warden's House...")
    
    # Close BAG
    bridge.press_buttons(["B", "sleep 500"])
    # Close START menu
    bridge.press_buttons(["Start", "sleep 500"])
    
    pos = get_pos()
    print(f"Position in Warden's House: {pos}")
    
    if pos is not None and pos[1] == 4:
        # Walk down and out
        print("Walking to exit...")
        bridge.press_buttons(["Down", "sleep 300", "Down", "sleep 300", "Down", "sleep 300"]) # to (2, 7)
        bridge.press_buttons(["Right", "sleep 300", "Right", "sleep 300"]) # to (4, 7)
        print("Stepping through door...")
        bridge.press_buttons(["Down", "sleep 1500"]) # exits Warden's House
        
    pos = get_pos()
    print(f"Emerged at: {pos}")

if __name__ == "__main__":
    main()
