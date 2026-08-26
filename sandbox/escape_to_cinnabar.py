import mgba
import time

def main():
    print("Opening Start menu...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Start", "sleep 1000"])
    
    # Since we just re-entered the overworld, the cursor should default to POKéDEX.
    # Press Down once to go to POKéMON and press A to enter.
    mgba.press_buttons(["Down", "sleep 350", "A", "sleep 1200"])
    
    # Press Down 5 times to go to TRUFFLE (Slot 6) and press A.
    mgba.press_buttons([
        "Down", "sleep 300",
        "Down", "sleep 300",
        "Down", "sleep 300",
        "Down", "sleep 300",
        "Down", "sleep 300",
        "A", "sleep 1000"
    ])
    
    # Press A to use DIG
    mgba.press_buttons(["A", "sleep 3500"])
    
    pos = mgba.get_coordinates()
    print("DIG executed. Current position:", pos)

if __name__ == "__main__":
    main()
