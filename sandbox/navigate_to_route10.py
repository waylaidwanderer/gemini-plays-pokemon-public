import mgba
import time
from PIL import Image

def get_current_pos():
    pos = mgba.get_coordinates()
    # If coordinates are 0,0, they might be invalid (e.g., in battle or transition)
    return pos['x'], pos['y']

def handle_battle_or_dialogue():
    print("Coordinate didn't change. Checking if in battle/dialogue/blocked...")
    # Press B to dismiss potential text/menus
    mgba.press_buttons(["B", "sleep 200"])
    # Press Down, Down, A to run from wild battle
    mgba.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "A", "sleep 1000"])
    # Press B again just in case
    mgba.press_buttons(["B", "sleep 200"])

def move_to(target_x, target_y):
    print(f"Moving towards target: ({target_x}, {target_y})")
    max_attempts_per_step = 10
    
    while True:
        curr_x, curr_y = get_current_pos()
        print(f"Current Position: ({curr_x}, {curr_y})")
        
        if curr_x == target_x and curr_y == target_y:
            print("Reached target!")
            break
            
        # Determine next step direction
        dx = target_x - curr_x
        dy = target_y - curr_y
        
        # We move along x first, or y first?
        # Let's move in the direction of the non-zero delta.
        # But wait, we have a specific path planned:
        # 1. Walk down to (29, 12)
        # 2. Walk right to (41, 12)
        # 3. Walk up to (41, 6)
        # 4. Walk right to (50, 6)
        # So we should strictly follow the coordinate sequence.
        
        # If we are doing sequence pathing, we can pass a list of waypoints.

def follow_path(waypoints):
    for i, wp in enumerate(waypoints):
        tx, ty = wp
        print(f"--- Heading to waypoint {i}: ({tx}, {ty}) ---")
        
        attempts = 0
        while True:
            cx, cy = get_current_pos()
            if cx == tx and cy == ty:
                print(f"Reached waypoint ({tx}, {ty})")
                break
                
            # If coordinates are 0,0, we might be in battle or transition
            if cx == 0 and cy == 0:
                print("Coordinates are (0,0). Attempting to dismiss battle/dialogue...")
                handle_battle_or_dialogue()
                continue
                
            # Determine direction to move
            if cx != tx:
                dir_btn = "Right" if tx > cx else "Left"
            else:
                dir_btn = "Down" if ty > cy else "Up"
                
            print(f"At ({cx}, {cy}). Stepping {dir_btn} towards ({tx}, {ty})")
            mgba.press_buttons([dir_btn, "sleep 300"])
            
            # Check if we moved
            nx, ny = get_current_pos()
            if nx == cx and ny == cy:
                attempts += 1
                if attempts > 3:
                    print("Stuck! Attempting to resolve battle or blockage...")
                    handle_battle_or_dialogue()
                    attempts = 0
            else:
                attempts = 0

if __name__ == "__main__":
    # Waypoints to Route 10
    path = [
        (29, 12),  # Down to Row 12
        (41, 12),  # Right to Column 41
        (41, 6),   # Up to Row 6
        (50, 6)    # Right to Route 10
    ]
    follow_path(path)
    
    # Let's take a screenshot at the end
    screenshot_file = mgba.take_screenshot()
    print(f"Finished navigation! Screenshot saved to {screenshot_file}")
    print(f"Final coordinates: {mgba.get_coordinates()}")
