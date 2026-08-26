import mgba
import time

def walk_to_col_10(target_col):
    # Safe pathing from any position to (target_col, 10) on 3F West
    # The statue at Column 2 blocks Row 10 and 11.
    # So to cross Column 2, we must use Row 13!
    current_pos = mgba.get_coordinates()
    print(f"Pathing from {current_pos} to ({target_col}, 10)...")
    
    # 1. Walk down to Row 13
    dy = 13 - current_pos["y"]
    if dy > 0:
        for _ in range(dy):
            mgba.press_buttons(["Down"])
            time.sleep(0.4)
            
    # 2. Walk horizontally on Row 13 to target_col
    current_pos = mgba.get_coordinates()
    dx = target_col - current_pos["x"]
    if dx > 0:
        for _ in range(dx):
            mgba.press_buttons(["Right"])
            time.sleep(0.4)
    elif dx < 0:
        for _ in range(-dx):
            mgba.press_buttons(["Left"])
            time.sleep(0.4)
            
    # 3. Walk UP Column target_col to Row 10
    current_pos = mgba.get_coordinates()
    dy = current_pos["y"] - 10
    if dy > 0:
        for _ in range(dy):
            mgba.press_buttons(["Up"])
            time.sleep(0.4)
            
    pos = mgba.get_coordinates()
    if pos["x"] == target_col and pos["y"] == 10:
        return True
    return False

def try_step(direction, expected_coords):
    mgba.press_buttons([direction])
    time.sleep(0.4)
    pos = mgba.get_coordinates()
    if pos == expected_coords:
        return True
    return False

pos = mgba.get_coordinates()
print("Starting position:", pos)

walkable_paths = {}

for col in range(1, 7):
    print(f"\n--- Testing Column {col} Row 9 ---")
    if walk_to_col_10(col):
        # Try to step UP to (col, 9)
        success = try_step("Up", {"x": col, "y": 9})
        walkable_paths[col] = success
        if success:
            print(f"RESULT: Column {col} Row 9 is WALKABLE!")
            # Walk back down to (col, 10)
            try_step("Down", {"x": col, "y": 10})
        else:
            print(f"RESULT: Column {col} Row 9 is BLOCKED.")
    else:
        print(f"Failed to reach ({col}, 10)")

print("\n===============================")
print("FINAL WALKABILITY RESULTS ON ROW 9:")
for col, walkable in walkable_paths.items():
    print(f"Column {col}: {'WALKABLE' if walkable else 'BLOCKED'}")
