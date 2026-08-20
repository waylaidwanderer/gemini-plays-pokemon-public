import mgba
import time

def handle_battle():
    print("Encountered battle or text! Escaping...")
    # First press A twice to dismiss intro text (in case battle just started)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Press B to close submenus, then Down, Right, A to run
    mgba.press_buttons(["B", "sleep 200", "Down", "Right", "A"])
    time.sleep(3.0)
    mgba.press_buttons(["B"])
    time.sleep(0.5)

def move_towards(tx, ty):
    """Moves one step towards target (tx, ty) from current position, handling battles."""
    pos = mgba.get_coordinates()
    cx, cy = pos['x'], pos['y']
    
    if cx == tx and cy == ty:
        return True
        
    # Decide direction
    if cx < tx:
        d = "Right"
        nx, ny = cx + 1, cy
    elif cx > tx:
        d = "Left"
        nx, ny = cx - 1, cy
    elif cy < ty:
        d = "Down"
        nx, ny = cx, cy + 1
    else:
        d = "Up"
        nx, ny = cx, cy - 1
        
    print(f"At ({cx}, {cy}). Stepping {d} towards ({tx}, {ty})...")
    mgba.press_buttons([d])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    
    if new_pos['x'] == nx and new_pos['y'] == ny:
        return True
        
    # Blocked or battle
    print("Movement blocked! Running escape sequence...")
    handle_battle()
    return False

def follow_waypoints(waypoints):
    """Follows a list of waypoints sequentially with robust error recovery."""
    for idx, (tx, ty) in enumerate(waypoints):
        print(f"--- Heading to Waypoint {idx+1}: ({tx}, {ty}) ---")
        attempts = 0
        while True:
            pos = mgba.get_coordinates()
            if pos['x'] == tx and pos['y'] == ty:
                print(f"Reached Waypoint {idx+1}!")
                break
                
            attempts += 1
            if attempts > 30:
                print(f"Failed to reach waypoint ({tx}, {ty}) after 30 attempts.")
                mgba.take_screenshot()
                return False
                
            move_towards(tx, ty)
    return True

def run_main():
    print("Starting robust waypoint routing to 2F stairs...")
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # 1. Escape the current Koffing/Ponyta battle (cursor is on FIGHT)
    print("Escaping current battle...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(3.0)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Position after initial escape:", pos)
    
    # 2. Waypoints to reach (7, 11) stairs area on 3F
    waypoints = [
        (23, 12),
        (19, 12),
        (19, 6),
        (11, 6),
        (11, 11),
        (7, 11)
    ]
    
    if not follow_waypoints(waypoints):
        return False
        
    # We are at (7, 11) on 3F. Let's test how to warp down to 2F.
    # First, try walking Up to (7, 10)
    print("At (7, 11). Walking Up to (7, 10)...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0) # wait for warp
    
    pos3 = mgba.get_coordinates()
    print("Position after walking Up:", pos3)
    
    if pos3['x'] == 7 and pos3['y'] == 10:
        # We did not warp. Try walking Up to (7, 9) and then Down to (7, 10)
        print("Did not warp. Walking Up to (7, 9)...")
        mgba.press_buttons(["Up"])
        time.sleep(0.5)
        print("Position:", mgba.get_coordinates())
        
        print("Walking Down onto (7, 10) stairs...")
        mgba.press_buttons(["Down"])
        time.sleep(2.0) # wait for warp
        
        final_pos = mgba.get_coordinates()
        print("Final position after Down warp attempt:", final_pos)
        mgba.take_screenshot()
    else:
        print("Successfully warped to 2F!")
        mgba.take_screenshot()

if __name__ == "__main__":
    run_main()
