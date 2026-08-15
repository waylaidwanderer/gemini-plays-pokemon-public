import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("Closing POKEDEX and navigating to Trainer Card...")
    # Close POKEDEX
    bridge.press_buttons(["B", "sleep 1000"])
    
    # Now we are on START menu, cursor is guaranteed on POKEDEX!
    print("Moving down 3 times to ACE...")
    for _ in range(3):
        bridge.press_buttons(["Down", "sleep 200"])
        
    print("Opening Trainer Card...")
    bridge.press_buttons(["A", "sleep 1500"])
    
    # Capture screenshot of Trainer Card
    mgba.take_screenshot()
    print("Trainer card screenshot captured.")

if __name__ == "__main__":
    main()
