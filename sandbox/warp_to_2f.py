import mgba
import time

def warp_now():
    print("Attempting to warp down to 2F from 3F...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Initial pos on 3F:", pos)
    
    # Press Up twice to turn and step UP
    mgba.press_buttons(["Up", "Up"])
    time.sleep(2.0) # Wait for warp animation
    
    new_pos = mgba.get_coordinates()
    print("Position after warp attempt:", new_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    warp_now()
