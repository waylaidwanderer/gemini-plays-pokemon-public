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

def move_to(target_x, target_y):
    # Attempt to move to an adjacent target tile. Handles battles and recalculations.
    for attempt in range(3):
        curr = mgba.get_coordinates()
        if curr == {'x': target_x, 'y': target_y}:
            return True
            
        dx = target_x - curr['x']
        dy = target_y - curr['y']
        
        if abs(dx) + abs(dy) != 1:
            print(f"Non-adjacent! Current: {curr}, Target: ({target_x}, {target_y}). Attempting to recover...")
            escape_battle()
            time.sleep(2.0)
            curr = mgba.get_coordinates()
            if curr == {'x': target_x, 'y': target_y}:
                return True
            dx = target_x - curr['x']
            dy = target_y - curr['y']
            if abs(dx) + abs(dy) != 1:
                print(f"Still non-adjacent after recovery check: {curr}")
                return False
            
        if dx == 1: direction = "Right"
        elif dx == -1: direction = "Left"
        elif dy == 1: direction = "Down"
        elif dy == -1: direction = "Up"
        
        print(f"Step Attempt {attempt+1}: Stepping {direction} from {curr} to ({target_x}, {target_y})...")
        mgba.press_buttons([direction])
        time.sleep(0.4)
        
        new_pos = mgba.get_coordinates()
        if new_pos == {'x': target_x, 'y': target_y}:
            return True
            
        print(f"Failed to reach target. Position is {new_pos}. Attempting escape...")
        escape_battle()
        time.sleep(2.0) # wait for overworld to reload
        
    return False

def walk_route(route_coords):
    for target in route_coords:
        curr = mgba.get_coordinates()
        if curr == target:
            continue
        if not move_to(target['x'], target['y']):
            print(f"Fatal: Failed to reach coordinate {target}")
            return False
        print(f"Successfully reached {target}")
    return True

# 1. Route to stairs at (5, 10) in State A from current (7, 8)
route_to_stairs = [
    {'x': 6, 'y': 8}, {'x': 5, 'y': 8},
    {'x': 5, 'y': 9}, {'x': 5, 'y': 10}
]

# 2. Route from (5, 11) to balcony drop (19, 18) on 3F in State A
route_to_balcony = [
    {'x': 6, 'y': 11}, {'x': 7, 'y': 11}, {'x': 8, 'y': 11}, {'x': 9, 'y': 11}, {'x': 10, 'y': 11}, {'x': 11, 'y': 11}, {'x': 12, 'y': 11},
    {'x': 12, 'y': 12}, {'x': 12, 'y': 13}, {'x': 12, 'y': 14}, {'x': 12, 'y': 15}, {'x': 12, 'y': 16},
    {'x': 13, 'y': 16}, {'x': 14, 'y': 16}, {'x': 15, 'y': 16}, {'x': 16, 'y': 16}, {'x': 17, 'y': 16}, {'x': 18, 'y': 16}, {'x': 19, 'y': 16}, {'x': 20, 'y': 16}, {'x': 21, 'y': 16},
    {'x': 21, 'y': 17}, {'x': 21, 'y': 18},
    {'x': 20, 'y': 18}, {'x': 19, 'y': 18}
]

print("Executing direct balcony drop script in State A starting from (7, 8)...")
print("Current Position:", mgba.get_coordinates())

print("Navigating to stairs...")
if walk_route(route_to_stairs):
    print("Warping to 3F West...")
    time.sleep(2.0) # wait for warp loading
    pos = mgba.get_coordinates()
    print("Landing position on 3F West:", pos)

    if pos == {'x': 5, 'y': 11}:
        print("Navigating to balcony drop at (19, 18) on 3F in State A...")
        if walk_route(route_to_balcony):
            print("Executed balcony drop successfully!")
            time.sleep(2.0) # wait for drop transition
            print("Final landing position on B1F West:", mgba.get_coordinates())
        else:
            print("Interrupted on 3F route to balcony.")
    else:
        print("Landing position is not (5, 11). Current position:", pos)
else:
    print("Failed to reach 2F stairs.")
