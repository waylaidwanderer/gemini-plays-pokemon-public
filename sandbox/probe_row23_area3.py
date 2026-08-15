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

def walk(direction):
    res = bridge.press_buttons([direction, "sleep 450"])
    pos = get_pos()
    return pos

def handle_textbox_or_battle():
    print("Coordinates are None. Handling potential battle or dialog...")
    # Clear text boxes with B
    for _ in range(5):
        bridge.press_buttons(["B", "sleep 150"])
    
    # Try to RUN
    print("Attempting to RUN from battle...")
    bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
    
    # Clear post-flee text
    for _ in range(3):
        bridge.press_buttons(["B", "sleep 150"])
        
    pos = get_pos()
    print(f"Coordinates after battle handling: {pos}")
    return pos

def walk_robust(direction):
    pos = get_pos()
    if pos is None:
        return handle_textbox_or_battle()
    pos_new = walk(direction)
    if pos_new is None:
        return handle_textbox_or_battle()
    if pos_new == pos:
        bridge.press_buttons(["B", "sleep 200"])
        pos_new = get_pos()
    return pos_new

def main():
    pos = get_pos()
    print(f"Starting systematic east probe from {pos}")
    
    # We are at (2, 23). Walk RIGHT to Column 19
    for col in range(3, 20):
        pos = walk_robust("Right")
        if pos is None or pos[0] != col:
            print(f"Blocked walking RIGHT at Column {col}")
            break
            
        print(f"At ({col}, 23), checking DOWN...")
        # Check if DOWN is open
        down_pos = walk_robust("Down")
        if down_pos is not None and down_pos[1] == 24:
            print(f"-> Column {col} Row 24 is OPEN!")
            # Check Row 25
            down_pos2 = walk_robust("Down")
            if down_pos2 is not None and down_pos2[1] == 25:
                print(f"-> Column {col} Row 25 is OPEN!")
                # Check Row 26
                down_pos3 = walk_robust("Down")
                if down_pos3 is not None and down_pos3[1] == 26:
                    print(f"-> SUCCESS! Column {col} is a complete passage to Row 26!")
                    return
                walk_robust("Up")
            walk_robust("Up")
            
    print("East probe complete.")

if __name__ == "__main__":
    main()
