import mgba
import time

def step_up():
    print("Pressing Up once with a delay...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Start pos:", pos)
    
    mgba.press_buttons(["Up"])
    time.sleep(2.0) # wait for movement/warp
    
    new_pos = mgba.get_coordinates()
    print("End pos:", new_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    step_up()
