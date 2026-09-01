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

# 3F Balcony Route in State A starting from (2, 12)
route_to_balcony = [
    {'x': 3, 'y': 12}, # RIGHT
    {'x': 3, 'y': 11}, # UP
    {'x': 4, 'y': 11}, {'x': 5, 'y': 11}, {'x': 6, 'y': 11}, {'x': 7, 'y': 11}, {'x': 8, 'y': 11}, {'x': 9, 'y': 11}, {'x': 10, 'y': 11}, {'x': 11, 'y': 11}, {'x': 12, 'y': 11}, # RIGHT along Row 11
    {'x': 12, 'y': 12}, {'x': 12, 'y': 13}, {'x': 12, 'y': 14}, {'x': 12, 'y': 15}, {'x': 12, 'y': 16}, # DOWN Column 12
    {'x': 13, 'y': 16}, {'x': 14, 'y': 16}, {'x': 15, 'y': 16}, {'x': 16, 'y': 16}, {'x': 17, 'y': 16}, {'x': 18, 'y': 16}, {'x': 19, 'y': 16}, {'x': 20, 'y': 16}, {'x': 21, 'y': 16}, # RIGHT along Row 16
    {'x': 21, 'y': 17}, {'x': 21, 'y': 18}, # DOWN past the open balcony gate!
    {'x': 20, 'y': 18}, {'x': 19, 'y': 18} # LEFT to Column 19 (drop!)
]

print("Executing 3F balcony drop navigation from (2, 12) in State A...")
print("Current Position:", mgba.get_coordinates())

if walk_route(route_to_balcony):
    print("Reached balcony drop tile (19, 18) successfully! Performing final drop step...")
    # Walking down or left from (19, 18) drops the player over the balcony railing to B1F West!
    # Let's walk DOWN once to execute the drop!
    mgba.press_buttons(["Down"])
    time.sleep(2.0) # wait generously for falling animation and map transition!
    
    final_pos = mgba.get_coordinates()
    print("Coordinates after balcony drop:", final_pos)
    mgba.take_screenshot()
else:
    print("Failed to reach balcony drop tile.")
    mgba.take_screenshot()
