import mgba
import time

def flee_battle():
    print("Fleeing battle...")
    # Press B to make sure we are not in some menu or sub-menu
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    
    # Try to flee by selecting RUN (Down, Right, then A)
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    # Dismiss any text with B
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)

if __name__ == "__main__":
    flee_battle()
