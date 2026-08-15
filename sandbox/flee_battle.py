import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import bridge
import mgba

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def main():
    print("Dismissing 'appeared!' text box...")
    bridge.press_buttons(["A", "sleep 1200"])
    
    # Try to flee
    print("Selecting RUN...")
    bridge.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1200"])
    
    pos = get_pos()
    print(f"Coordinates after flee attempt: {pos}")
    
    # If still in battle (coordinates are None), try again
    attempts = 0
    while pos is None and attempts < 5:
        print("Still in battle or textbox on screen. Clearing textbox and attempting RUN again...")
        # Press B a few times to clear post-flee text or other dialogs
        for _ in range(3):
            bridge.press_buttons(["B", "sleep 200"])
        
        # Press A once to make sure menu is active
        bridge.press_buttons(["A", "sleep 500"])
        
        # Select RUN
        bridge.press_buttons(["Down", "sleep 200", "Right", "sleep 200", "A", "sleep 1200"])
        pos = get_pos()
        print(f"Coordinates after attempt {attempts+1}: {pos}")
        attempts += 1
        
    print(f"Flee sequence complete. Position: {pos}")

if __name__ == "__main__":
    main()
