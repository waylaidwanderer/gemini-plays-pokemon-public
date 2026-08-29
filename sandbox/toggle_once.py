import mgba
import time

def main():
    print("toggle_once: Toggling switch to State B...")
    # Stand at (2, 12) facing UP and press A 4 times with 1.0s delay
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    print("toggle_once: Finished.")

if __name__ == "__main__":
    main()
