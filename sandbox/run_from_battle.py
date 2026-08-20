import mgba
import time

def run_battle():
    print("Dismissing 'Wild PONYTA appeared!' text...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    print("Dismissing player sending out Pokemon text...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    print("Moving cursor to RUN and executing...")
    # Menu layout: FIGHT is top-left, RUN is bottom-right.
    # From FIGHT (default): Down, Right, A
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(2.0)
    
    # Dismiss any leftover text/menus
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Position after run attempt:", pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    run_battle()
