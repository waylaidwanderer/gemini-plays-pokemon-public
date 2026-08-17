import mgba
import time

def press_and_wait(button, delay=0.25):
    mgba.press_buttons([button])
    time.sleep(delay)

def get_pos():
    pos = mgba.get_coordinates()
    return pos['x'], pos['y']

def walk_to(target_x, target_y):
    print(f"Walking to ({target_x}, {target_y})...")
    for attempt in range(40):
        cx, cy = get_pos()
        if cx == target_x and cy == target_y:
            print(f"Arrived at ({cx}, {cy})")
            return True
            
        dx = target_x - cx
        dy = target_y - cy
        
        # Try to move horizontally first
        if dx != 0:
            btn = "Right" if dx > 0 else "Left"
            press_and_wait(btn, 0.3)
            nx, ny = get_pos()
            if nx == cx and ny == cy:
                # We bumped! Try to go vertically to bypass obstacle
                print(f"Bumped moving horizontally at ({cx}, {cy}). Trying vertical detour.")
                btn_alt = "Down" if cy < 5 else "Up"
                press_and_wait(btn_alt, 0.3)
        elif dy != 0:
            btn = "Down" if dy > 0 else "Up"
            press_and_wait(btn, 0.3)
            nx, ny = get_pos()
            if nx == cx and ny == cy:
                # We bumped! Try to go horizontally to bypass obstacle
                print(f"Bumped moving vertically at ({cx}, {cy}). Trying horizontal detour.")
                btn_alt = "Right" if cx < 10 else "Left"
                press_and_wait(btn_alt, 0.3)
                
    print("Failed to reach target in 40 steps.")
    return False

def take_stairs():
    # To trigger a staircase/warp, we just step into it.
    # Usually the stairs tile is at y=1, and we step Up into it.
    cx, cy = get_pos()
    print(f"At ({cx}, {cy}), stepping UP into stairs...")
    press_and_wait("Up", 1.0) # Wait longer for map transition
    nx, ny = get_pos()
    print(f"After stairs transition, position is: ({nx}, {ny})")
    return nx != cx or ny != cy

def climb_department_store():
    # 1. We are currently at (3, 3) on 2F.
    # We need to go to stairs at (16, 1) to go to 3F.
    cx, cy = get_pos()
    print(f"Starting climb from ({cx}, {cy})")
    
    # 2F -> 3F (UP stairs at 16, 1)
    if cy > 1: # We are still on 2F (or similar)
        print("--- 2F to 3F ---")
        walk_to(16, 2)
        take_stairs()
        
    # 3F -> 4F (UP stairs at 12, 1)
    cx, cy = get_pos()
    print(f"Current pos: ({cx}, {cy})")
    print("--- 3F to 4F ---")
    walk_to(12, 2)
    take_stairs()
    
    # 4F -> 5F (UP stairs at 16, 1)
    cx, cy = get_pos()
    print(f"Current pos: ({cx}, {cy})")
    print("--- 4F to 5F ---")
    walk_to(16, 2)
    take_stairs()
    
    # 5F -> Roof (UP stairs at 12, 1)
    cx, cy = get_pos()
    print(f"Current pos: ({cx}, {cy})")
    print("--- 5F to Roof ---")
    walk_to(12, 2)
    take_stairs()
    
    # Now we should be on the Roof!
    cx, cy = get_pos()
    print(f"Arrived on Roof at ({cx}, {cy})")
    
    # From (15, 2) on Roof, walk to vending machine
    print("--- Navigating on Roof ---")
    # Walk down to row 3 to avoid stairs warp
    press_and_wait("Down", 0.3)
    walk_to(9, 3)
    walk_to(6, 3)
    # Walk UP to row 2 to face the vending machine
    walk_to(6, 2)
    # Vending machine interaction
    print("Facing vending machine. Pressing A...")
    press_and_wait("A", 1.0) # Open vending machine menu
    
    # Vending machine menu options:
    # 1. FRESH WATER (¥200)
    # 2. SODA POP (¥300)
    # 3. LEMONADE (¥350)
    # 4. CANCEL
    # Let's select Option 1 (Fresh Water)
    print("Selecting Fresh Water (Option 1)...")
    press_and_wait("A", 0.5) # Select option 1
    # Vending machine dialogue: "A can of FRESH WATER popped out!"
    print("Confirming dialogue...")
    press_and_wait("A", 1.0)
    press_and_wait("A", 1.0)
    
    # Let's buy a second Fresh Water or another drink just in case!
    print("Interacting with vending machine again...")
    press_and_wait("A", 1.0)
    print("Selecting Soda Pop (Option 2)...")
    press_and_wait("Down", 0.3)
    press_and_wait("A", 0.5)
    print("Confirming Soda Pop dialogue...")
    press_and_wait("A", 1.0)
    press_and_wait("A", 1.0)
    
    print("Exiting vending machine...")
    press_and_wait("B", 0.5)
    
    mgba.take_screenshot()
    print("Vending machine purchase completed successfully!")

climb_department_store()
