import mgba
import time

def get_current_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def handle_potential_battle():
    # If we are stuck or coordinates are (0,0), we might be in battle.
    # Let's mash A and B to either fight or dismiss text.
    print("Handling battle or dialogue...")
    for _ in range(15):
        mgba.press_buttons(["A", "sleep 200", "B", "sleep 200"])

def step_to(tx, ty):
    cx, cy = get_current_pos()
    if cx == tx and cy == ty:
        return True
        
    if cx == 0 and cy == 0:
        handle_potential_battle()
        return False
        
    # Determine direction
    if cx != tx:
        btn = "Right" if tx > cx else "Left"
    else:
        btn = "Down" if ty > cy else "Up"
        
    print(f"Stepping {btn} from ({cx}, {cy}) to ({tx}, {ty})")
    mgba.press_buttons([btn, "sleep 400"])
    
    nx, ny = get_current_pos()
    if nx == cx and ny == cy:
        # We didn't move. Could be blocked or in battle.
        print("Movement failed. Retrying...")
        handle_potential_battle()
        return False
    return True

def follow_path(waypoints):
    for wp in waypoints:
        tx, ty = wp
        print(f"Heading to waypoint ({tx}, {ty})")
        while True:
            cx, cy = get_current_pos()
            if cx == tx and cy == ty:
                break
            step_to(tx, ty)

if __name__ == "__main__":
    path = [
        (41, 7),  # Left to Col 41
        (41, 3),  # Up to Row 3
        (50, 3)   # Right to Route 10
    ]
    follow_path(path)
    print(f"Navigation complete! Current position: {mgba.get_coordinates()}")
