import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 400"])

def probe():
    # Currently at (26, 12)
    print("Starting probe...")
    
    # 1. Walk Left to Column 25
    walk_step("Left")
    print(f"Pos after Left: {get_pos()}")
    
    # 2. Walk UP 2 steps to row 10 (Wait, (25, 12) to (25, 11) to (25, 10))
    # Wait, can we walk UP from (25, 12) to (25, 11)?
    # In our previous script, we tried UP on column 25 from (25, 12) and it stayed at (25, 12)!
    # Let's see if column 25 is blocked on the north edge too.
    # If column 25 is blocked, can we walk Left more on the Plateau?
    # Column 24 is the stairs. Let's walk Left to column 24: (25, 12) -> (24, 12).
    # And then walk Down the stairs: (24, 12) -> (24, 15) -> (24, 16) (ground level).
    # Then walk to row 10 on the ground!
    # Yes! Walk down to (24, 16), then walk:
    # Left to Column 23, then walk UP to Row 10 on column 23?
    # Wait, is column 23 open on rows 10-15?
    # Let's check!
    
    # Let's just walk back to ground level first
    print("Walking back to ground level at (24, 16)...")
    walk_step("Left") # To (25, 12)
    walk_step("Left") # To (24, 12)
    walk_step("Down") # To (24, 13)
    walk_step("Down") # To (24, 14)
    walk_step("Down") # To (24, 15)
    walk_step("Down") # To (24, 16)
    print(f"Back on ground: {get_pos()}")
    
    # Now we are at (24, 16).
    # We want to go to the building at row 10 on column 25 or 26.
    # Can we walk to the left of the Plateau?
    # Let's try walking Left and see where we can go UP!
    # Let's walk Left 4 steps: to column 20.
    for _ in range(4):
        walk_step("Left")
    print(f"Pos: {get_pos()}")
    
    # Walk UP column 20 as far as possible!
    print("Walking UP column 20...")
    for i in range(12):
        pos = get_pos()
        walk_step("Up")
        new_pos = get_pos()
        print(f"Step {i}: before={pos}, after={new_pos}")
        if new_pos == pos:
            print("Blocked!")
            break

if __name__ == "__main__":
    probe()
