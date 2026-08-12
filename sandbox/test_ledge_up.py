import bridge
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is not None:
        return pos[0], pos[1]
    return None

def test_up_at_col(col):
    print(f"--- Testing UP at Column {col} ---")
    pos = get_pos()
    if pos is None:
        return
        
    # Align to the target column on Row 32
    current_col = pos[0]
    steps = col - current_col
    if steps > 0:
        for _ in range(steps):
            bridge.press_buttons(["Right"])
            time.sleep(0.5)
    elif steps < 0:
        for _ in range(-steps):
            bridge.press_buttons(["Left"])
            time.sleep(0.5)
            
    pos = get_pos()
    if pos is not None and pos[0] == col and pos[1] == 32:
        # Try to walk UP
        bridge.press_buttons(["Up"])
        time.sleep(0.6)
        pos_after = get_pos()
        if pos_after is not None and pos_after[1] < 32:
            print(f"SUCCESS! Walked UP at Column {col} to {pos_after}!")
            # Walk back down
            bridge.press_buttons(["Down"])
            time.sleep(0.5)
            return True
        else:
            print(f"Blocked at Column {col}!")
    else:
        print(f"Failed to align to ({col}, 32). Current pos: {pos}")
    return False

def main():
    # We are currently at (23, 32)
    # Let's test Columns 23 down to 16
    for col in range(23, 15, -1):
        if test_up_at_col(col):
            print(f"Found a walkable gap at Column {col}!")
            break

if __name__ == "__main__":
    main()
