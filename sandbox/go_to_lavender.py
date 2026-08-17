import mgba
import time

def walk_to_lavender():
    print("Walking north to Lavender Town...")
    for step in range(20):
        pos = mgba.get_coordinates()
        if not pos:
            print("Failed to get coordinates, stopping.")
            break
        x, y = pos['x'], pos['y']
        print(f"Current Position: {x}, {y}")
        
        # Check if we transitioned to Lavender Town
        # In Lavender Town, our coordinates will warp to around y=16 (transition from y=0 on Route 12)
        # If the map transition is detected, get_coordinates will reflect it.
        # But wait! If we transition to Lavender Town, the map changes.
        # Let's check if we are at y=0, then 1 more step UP triggers map transition.
        if y == 0:
            print("Reached y=0 on Route 12, taking final step to transition...")
            mgba.press_buttons(["Up"])
            time.sleep(1.0)
            break
            
        mgba.press_buttons(["Up"])
        time.sleep(0.4)
        
        new_pos = mgba.get_coordinates()
        if not new_pos:
            print("Failed to get coordinates after move, stopping.")
            break
        new_x, new_y = new_pos['x'], new_pos['y']
        
        if new_x == x and new_y == y:
            print(f"Movement failed at ({x}, {y}). Might be blocked, in a battle, or map transition.")
            mgba.take_screenshot()
            break

walk_to_lavender()
