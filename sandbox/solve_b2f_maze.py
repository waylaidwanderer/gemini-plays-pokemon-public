import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(1.0) # wait for movement/slide
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print("Starting B2F maze solving from:", pos)

if pos['x'] == 2 and pos['y'] == 9:
    # Step 1: Walk to (3, 11)
    pos = move(["Right"])
    pos = move(["Down"])
    pos = move(["Down"])
    
    # Step 2: Step onto (4, 11) RIGHT spinner
    print("Stepping onto (4, 11) RIGHT spinner...")
    pos = move(["Right"])
    time.sleep(2.0)
    pos = mgba.get_coordinates()
    print("Position after slide 1:", pos)

mgba.take_screenshot()
