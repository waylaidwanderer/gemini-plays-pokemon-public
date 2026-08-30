import mgba
import time

def flee_battle():
    print("Fleeing battle...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.4)
    
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(2.0)
    
    for _ in range(3):
        mgba.press_buttons(["B"])
        time.sleep(0.4)

flee_battle()
pos = mgba.get_coordinates()
print(f"Position after fleeing: {pos}")
mgba.take_screenshot()
