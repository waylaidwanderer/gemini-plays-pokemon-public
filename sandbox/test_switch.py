import mgba
import time

def main():
    print("Testing DOWN to (26, 4) in State B...")
    pos_before = mgba.get_coordinates()
    mgba.press_buttons(["Down"])
    time.sleep(1.0)
    pos_after = mgba.get_coordinates()
    print(f"Position before: {pos_before}, after: {pos_after}")
    
    if pos_before == pos_after:
        print("Bumped! (26, 4) is solid/blocked.")
    else:
        # Check if we fell
        # If we fell, the map changes or we land on 1F.
        # On 1F East inside the fenced room, can we walk to (25, 4)?
        # Let's test walking Left to (25, 4)
        print("Trying to step Left to (25, 4)...")
        mgba.press_buttons(["Left"])
        time.sleep(1.0)
        pos_left = mgba.get_coordinates()
        print(f"Position after Left: {pos_left}")
        if pos_left['x'] == 25 and pos_left['y'] == 4:
            print("Successfully walked Left on 1F East!")
        else:
            print("Failed to walk Left. We might still be on 3F East or stuck.")

if __name__ == "__main__":
    main()
