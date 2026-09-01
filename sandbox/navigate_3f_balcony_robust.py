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

# 3F Route from current (10, 17) to balcony (19, 18) in State A via Row 3 and Column 26
route_to_balcony = [
    # 1. UP Column 10 to Row 3
    {'x': 10, 'y': 16}, {'x': 10, 'y': 15}, {'x': 10, 'y': 14}, {'x': 10, 'y': 13}, {'x': 10, 'y': 12}, {'x': 10, 'y': 11}, {'x': 10, 'y': 10}, {'x': 10, 'y': 9}, {'x': 10, 'y': 8}, {'x': 10, 'y': 7}, {'x': 10, 'y': 6}, {'x': 10, 'y': 5}, {'x': 10, 'y': 4}, {'x': 10, 'y': 3},
    # 2. RIGHT Row 3 to Column 26
    {'x': 11, 'y': 3}, {'x': 12, 'y': 3}, {'x': 13, 'y': 3}, {'x': 14, 'y': 3}, {'x': 15, 'y': 3}, {'x': 16, 'y': 3}, {'x': 17, 'y': 3}, {'x': 18, 'y': 3}, {'x': 19, 'y': 3}, {'x': 20, 'y': 3}, {'x': 21, 'y': 3}, {'x': 22, 'y': 3}, {'x': 23, 'y': 3}, {'x': 24, 'y': 3}, {'x': 25, 'y': 3}, {'x': 26, 'y': 3},
    # 3. DOWN Column 26 to Row 12
    {'x': 26, 'y': 4}, {'x': 26, 'y': 5}, {'x': 26, 'y': 6}, {'x': 26, 'y': 7}, {'x': 26, 'y': 8}, {'x': 26, 'y': 9}, {'x': 26, 'y': 10}, {'x': 26, 'y': 11}, {'x': 26, 'y': 12},
    # 4. LEFT Row 12 to Column 24
    {'x': 25, 'y': 12}, {'x': 24, 'y': 12},
    # 5. DOWN Column 24 to Row 16
    {'x': 24, 'y': 13}, {'x': 24, 'y': 14}, {'x': 24, 'y': 15}, {'x': 24, 'y': 16},
    # 6. LEFT Row 16 to Column 21
    {'x': 23, 'y': 16}, {'x': 22, 'y': 16}, {'x': 21, 'y': 16},
    # 7. DOWN past open balcony gate at (21, 16) to Row 18
    {'x': 21, 'y': 17}, {'x': 21, 'y': 18},
    # 8. LEFT along Row 18 to Column 19 (drop tile)
    {'x': 20, 'y': 18}, {'x': 19, 'y': 18}
]

print("Executing robust 3F West-to-East balcony drop navigation in State A...")
print("Current Position:", mgba.get_coordinates())

if walk_route(route_to_balcony):
    print("Reached balcony drop tile (19, 18) successfully! Performing final drop step...")
    mgba.press_buttons(["Down"])
    time.sleep(2.5) # wait generously for drop transition!
    print("Final landing position on B1F West:", mgba.get_coordinates())
    mgba.take_screenshot()
else:
    print("Failed to reach balcony drop tile.")
    mgba.take_screenshot()
