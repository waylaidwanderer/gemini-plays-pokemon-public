import mgba
import time

def run():
    print("--- WALKING EAST THROUGH GATEHOUSE ---")
    pos = mgba.get_coordinates()
    print("Start position:", pos)
    
    # We are at (0, 9). Walk Right step-by-step up to 10 steps to find the east exit or transition.
    for i in range(10):
        mgba.press_buttons(["Right"])
        time.sleep(0.35)
        curr = mgba.get_coordinates()
        print(f"Step {i+1} Right: {curr}")
        if curr['x'] < pos['x'] - i:
            # We transitioned!
            print("Successfully transitioned!")
            break
            
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
