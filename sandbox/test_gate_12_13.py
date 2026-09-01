import mgba
import time

def escape_battle():
    print("Dismissing first screen text...")
    mgba.press_buttons(["B"])
    time.sleep(1.0)

    print("Dismissing second screen text...")
    mgba.press_buttons(["B"])
    time.sleep(3.0) # wait for SHELLBY send-out animation

    print("Selecting RUN...")
    mgba.press_buttons(["Down"])
    time.sleep(0.3)
    mgba.press_buttons(["Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(2.5) # wait for escape text

    print("Dismissing escape text...")
    mgba.press_buttons(["B"])
    time.sleep(1.5)

def step(direction):
    current = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.5)
    next_pos = mgba.get_coordinates()
    if next_pos == current:
        print(f"Blocked at {current}. Attempting battle escape...")
        escape_battle()
        time.sleep(2.0)
        mgba.press_buttons([direction])
        time.sleep(0.5)
        next_pos = mgba.get_coordinates()
    return next_pos

def walk_route(route_coords):
    for target in route_coords:
        curr = mgba.get_coordinates()
        if curr == target:
            continue
        dx = target['x'] - curr['x']
        dy = target['y'] - curr['y']
        
        if abs(dx) + abs(dy) == 1:
            if dx == 1: direction = "Right"
            elif dx == -1: direction = "Left"
            elif dy == 1: direction = "Down"
            elif dy == -1: direction = "Up"
            
            res = step(direction)
            if res != target:
                print(f"Failed to reach target {target}. Position: {res}")
                return False
            print(f"Reached {target}")
        else:
            print(f"Non-adjacent target {target} from {curr}")
            return False
    return True

# Ensure we are at (12, 12)
print("Navigating to (12, 12)...")
if walk_route([{'x': 12, 'y': 12}]):
    print("Successfully standing at (12, 12).")
    
    # Try to step Down to (12, 13)
    # We will do a clean step without the default automatic escape inside step()
    # so we can control exactly what happens
    curr = mgba.get_coordinates()
    mgba.press_buttons(["Down"])
    time.sleep(0.5)
    pos = mgba.get_coordinates()
    
    if pos == {'x': 12, 'y': 13}:
        print("GATE (12, 13) IS OPEN IN STATE A!")
        mgba.take_screenshot()
    elif pos == curr:
        # We got blocked. Was it a battle or a wall?
        # Let's wait a bit to see if screen shows battle
        print("Blocked at (12, 12). Checking if battle...")
        # Since we can't easily check battle state in python, let's try to escape anyway.
        # If it's a battle, escape will work and we will end up elsewhere.
        # If it's a solid wall, escape_battle will just press buttons and we will still be at (12, 12).
        escape_battle()
        time.sleep(2.0)
        new_pos = mgba.get_coordinates()
        if new_pos == {'x': 12, 'y': 12}:
            print("GATE (12, 13) IS CLOSED IN STATE A (Solid barrier!).")
            mgba.take_screenshot()
        else:
            print(f"Displaced to {new_pos} by battle escape. Let's try to run this test again!")
            mgba.take_screenshot()
    else:
        print(f"Unexpected move to {pos}")
        mgba.take_screenshot()
else:
    print("Failed to reach (12, 12).")
    mgba.take_screenshot()
