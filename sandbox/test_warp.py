import mgba
import time

def test_warp():
    # Currently at (5, 10)
    # We will step around the 4x5 carpet room (Columns 4-7, Rows 10-14)
    # to see if any tile triggers a warp.
    print("Testing steps in the southwest room...")
    
    steps = [
        "Down", # (5, 11)
        "Down", # (5, 12)
        "Right", # (6, 12)
        "Up", # (6, 11)
        "Up", # (6, 10)
        "Right", # (7, 10)
        "Down", # (7, 11)
        "Left", # (6, 11)
        "Left", # (5, 11)
        "Up", # (5, 10)
    ]
    
    for direction in steps:
        pos = mgba.get_coordinates()
        print(f"Current: {pos} | Pressing: {direction}")
        mgba.press_buttons([direction])
        time.sleep(0.6)
        new_pos = mgba.get_coordinates()
        print(f"New position: {new_pos}")
        if new_pos != pos and abs(new_pos['x'] - pos['x']) + abs(new_pos['y'] - pos['y']) > 1:
            print("Warp triggered! New position is:", new_pos)
            return

    print("No warp triggered in the tested area.")

if __name__ == "__main__":
    test_warp()
