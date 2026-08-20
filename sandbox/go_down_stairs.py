import mgba
import time

def step_down_and_warp():
    print("Attempting to step DOWN onto stairs from (6, 11)...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Initial pos at (6, 11):", pos)
    
    # Press Down twice to turn and step DOWN
    mgba.press_buttons(["Down", "Down"])
    time.sleep(2.0) # wait for warp
    
    new_pos = mgba.get_coordinates()
    print("Position after warp attempt:", new_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    step_down_and_warp()
