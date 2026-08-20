import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Current pos before toggle:", get_pos())

# Walk Down to (1, 11)
mgba.press_buttons(["Down"])
time.sleep(0.6)
print("Position after Down:", get_pos())

# Turn Right to face the switch
mgba.press_buttons(["Right"])
time.sleep(0.5)

# Interact with A
mgba.press_buttons(["A"])
time.sleep(1.2) # Let the YES/NO menu load completely

# Press Up to select YES (since default is NO)
mgba.press_buttons(["Up"])
time.sleep(0.5)

# Press A to select YES
mgba.press_buttons(["A"])
time.sleep(1.5) # Let the click text print completely

# Press B to clear the click text
mgba.press_buttons(["B"])
time.sleep(0.5)

# Press B again to ensure dialogue is fully closed
mgba.press_buttons(["B"])
time.sleep(0.5)

print("Toggle process complete! Current pos:", get_pos())
mgba.take_screenshot()
