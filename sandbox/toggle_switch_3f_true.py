import mgba
import time

def main():
    print("Starting correct switch toggle sequence on 3F...")
    
    # 1. Walk from (2, 10) to (2, 12)
    # We are currently at (2, 10).
    print("Moving Down to (2, 12)...")
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Coordinates at stand position:", pos)
    
    if pos == {'x': 2, 'y': 12}:
        # We walked Down, so we are currently facing DOWN at (2, 12).
        # We need to turn face UP, then press A!
        print("Turning face UP, waiting, and pressing A to toggle switch...")
        # "Up" turns us face UP in place.
        # "sleep 250" lets the turn animation finish.
        # "A" interacts with (2, 11).
        # "sleep 600" lets the dialogue open.
        # "A" selects YES to press the switch.
        # "sleep 600", "B" closes the dialogue box.
        mgba.press_buttons(["Up", "sleep 250", "A", "sleep 600", "A", "sleep 600", "B"])
        time.sleep(2.5)
        
        # Take a screenshot to verify
        print("Taking final screenshot of toggle attempt...")
        mgba.take_screenshot()
        print("Done!")
    else:
        print("Failed to reach (2, 12)!")
        mgba.take_screenshot()

if __name__ == "__main__":
    main()
