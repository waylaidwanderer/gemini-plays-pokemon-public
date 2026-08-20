import mgba
import time

def warp_now():
    print("Pressing Down once to warp...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Start pos on 3F:", pos)
    
    mgba.press_buttons(["Down"])
    time.sleep(2.5) # Wait for warp animation
    
    new_pos = mgba.get_coordinates()
    print("Position after warp:", new_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    warp_now()
