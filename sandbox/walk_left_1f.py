import mgba
import time

def run():
    print("--- WALKING LEFT ON 1F ---")
    pos = mgba.get_coordinates()
    print("Start position on 1F:", pos)
    
    # We are at (7, 7). Let's walk Left up to 8 steps to find the west exit or see if we get stopped.
    for i in range(8):
        mgba.press_buttons(["Left"])
        time.sleep(0.35)
        curr = mgba.get_coordinates()
        print(f"Step {i+1} Left: {curr}")
        if curr['x'] < pos['x'] - i:
            # We transitioned or stopped changing x
            pass
            
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
