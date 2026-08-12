import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("=== INTERACTING WITH THE WARDEN TO RECEIVE STRENGTH ===")
    
    # We are already at (2, 4) facing UP, in front of the Warden at (2, 3).
    # Press A to start talking
    bridge.press_buttons(["A"])
    time.sleep(1.0)
    
    # Progress dialogue (press A 15 times with 1.2s delay to fully receive HM04)
    for i in range(15):
        print(f"Dialogue step {i+1}...")
        bridge.press_buttons(["A"])
        time.sleep(1.2)
        
    print("=== CONGRATULATIONS! WARDEN DIALOGUE COMPLETED ===")

if __name__ == "__main__":
    main()
