import mgba
import time

print("Current coordinates:", mgba.get_coordinates())

# Bypass route to 1F East:
# (12, 11) -> (12, 6) -> (18, 6) -> (18, 4) -> (20, 4) -> (20, 3) -> (26, 3)
# Then DOWN Column 26 to Row 11: (26, 11)
# Then LEFT Row 11 to Column 18: (18, 11)
# Then UP Row 11 to Row 10: (18, 10) (stairs)
master_bypass_route = [
    (12, 6),
    (18, 6),
    (18, 4),
    (20, 4),
    (20, 3),
    (26, 3),
    (26, 11),
    (18, 11),
    (18, 10)
]

for wp in master_bypass_route:
    tx, ty = wp
    print(f"Walking to waypoint ({tx}, {ty})...")
    attempts = 0
    while attempts < 25:
        pos = mgba.get_coordinates()
        cur = (pos['x'], pos['y'])
        if cur == (tx, ty):
            break
            
        dx = tx - cur[0]
        dy = ty - cur[1]
        
        if dx < 0: direction = "Left"
        elif dx > 0: direction = "Right"
        elif dy < 0: direction = "Up"
        elif dy > 0: direction = "Down"
        else:
            break
            
        pos_before = pos
        mgba.press_buttons([direction])
        time.sleep(0.55)
        pos = mgba.get_coordinates()
        print(f"Moved to {pos}")
        
        if pos == pos_before:
            print("BUMPED or BATTLE! Stopping test.")
            break
        attempts += 1
