import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge

def main():
    print("Selecting POKEMON from the START menu...")
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 1000"]) # POKÉMON
    
    print("Selecting TRUFFLE (slot 2)...")
    bridge.press_buttons(["Down", "sleep 300", "A", "sleep 1000"]) # TRUFFLE
    
    print("Selecting DIG...")
    bridge.press_buttons(["A", "sleep 4000"]) # DIG
    
    # Wait for warp to complete
    time.sleep(1.0)
    print(f"Position after DIG warp: {bridge.get_coordinates()}")

if __name__ == "__main__":
    main()
