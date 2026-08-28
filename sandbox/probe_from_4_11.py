import mgba
import time

def get_pos():
    pos = mgba.get_coordinates()
    return (pos['x'], pos['y'])

def step(direction):
    old_pos = get_pos()
    print(f"Current: {old_pos}. Stepping {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.45)
    new_pos = get_pos()
    print(f"New position: {new_pos}")
    return new_pos

print(f"Starting probe from (4, 11). Current position: {get_pos()}")

# 1. Walk (4, 11) -> (4, 10) -> (5, 10) -> (5, 9)
step("Up")
step("Right")
step("Up")

pos = get_pos()
if pos == (5, 9):
    print("Successfully reached (5, 9). Probing...")
    step("Up") # to (5, 8)
    
    # Try Up from (5, 8) to (5, 7)
    step("Up")
    if get_pos() == (5, 7):
        print("Success! (5, 7) is walkable!")
        step("Down")
    else:
        print("(5, 7) is BLOCKED")
        
    # Walk Right to (6, 8)
    step("Right")
    
    # Try Up from (6, 8) to (6, 7)
    step("Up")
    if get_pos() == (6, 7):
        print("Success! (6, 7) is walkable!")
        step("Down")
    else:
        print("(6, 7) is BLOCKED")
        
    # Walk Right to (7, 8)
    step("Right")
    
    # Try Up from (7, 8) to (7, 7)
    step("Up")
    if get_pos() == (7, 7):
        print("Success! (7, 7) is walkable!")
        step("Down")
    else:
        print("(7, 7) is BLOCKED")
else:
    print("Failed to reach (5, 9)!")

mgba.take_screenshot()
