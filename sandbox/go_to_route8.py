import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def go_to_celadon():
    print("Walking west along Route 7 into Celadon City...")
    # Current Position is (5, 14) on Route 7
    # Walking LEFT 10 steps will ensure we transition to Celadon City
    for i in range(10):
        pos = mgba.get_coordinates()
        if pos:
            print(f"Current Position: {pos['x']}, {pos['y']}")
        press_and_wait("Left", 0.25)
        
    # Check new position
    pos = mgba.get_coordinates()
    if pos:
        print(f"Final Position: {pos['x']}, {pos['y']}")
    mgba.take_screenshot()

go_to_celadon()
