import mgba
import time

def flee_battle():
    mgba.press_buttons(["B", "B", "B", "Down", "Right", "A", "B", "sleep 300", "B"])

def step_to(target_x, target_y, max_tries=50):
    for t in range(max_tries):
        pos = mgba.get_coordinates()
        cx, cy = pos['x'], pos['y']
        if cx == target_x and cy == target_y:
            print(f"Reached target ({target_x}, {target_y})")
            return True
        
        # Decide direction
        btn = None
        if cx < target_x:
            btn = "Right"
        elif cx > target_x:
            btn = "Left"
        elif cy < target_y:
            btn = "Down"
        elif cy > target_y:
            btn = "Up"
            
        p_before = pos
        mgba.press_buttons([btn])
        p_after = mgba.get_coordinates()
        
        if p_before == p_after:
            # Handle possible battle
            flee_battle()
            p_after = mgba.get_coordinates()
            if p_before == p_after:
                print(f"Blocked at {p_before} trying to move {btn} towards ({target_x}, {target_y})")
                return False
    return False

# Route:
# 1. Move to (10, 14)
# 2. Move to (11, 14)
# 3. Move to (11, 6)
# 4. Move East along row 6 to (37, 6)
# 5. Move South along col 37 to (37, 17)

pos = mgba.get_coordinates()
print(f"Start at: {pos}")

print("Leg 1: to (10, 14)")
step_to(10, 14)

print("Leg 2: to (11, 14)")
step_to(11, 14)

print("Leg 3: to (11, 6)")
step_to(11, 6)

print("Leg 4: to (37, 6)")
step_to(37, 6)

print("Leg 5: to (37, 17)")
step_to(37, 17)

print("Final pos:", mgba.get_coordinates())
