import bridge
import time

def cut_bush():
    print("Cutting bush at (26, 13)...")
    bridge.press_buttons(["Up"])
    time.sleep(0.4)
    bridge.press_buttons(["Start"])
    time.sleep(0.5)
    bridge.press_buttons(["Up", "A", "sleep 800", "Down", "A", "sleep 800", "A"]) # Use CUT on TRUFFLE
    time.sleep(2.0)
    bridge.press_buttons(["A"])
    time.sleep(0.5)
    print("Bush cut successfully.")

def walk_to_waypoint(target_x, target_y):
    print(f"Navigating to waypoint ({target_x}, {target_y})...")
    stuck_count = 0
    last_coords = None
    
    while True:
        curr = bridge.get_coordinates()
        if curr is None:
            print("Coordinates are None. Waiting...")
            time.sleep(0.5)
            continue
            
        x, y = curr
        if x == target_x and y == target_y:
            print(f"Reached waypoint ({target_x}, {target_y})")
            return True
            
        if curr == last_coords:
            stuck_count += 1
            if stuck_count > 4:
                print(f"Stuck at {curr} trying to reach ({target_x}, {target_y})")
                return False
        else:
            stuck_count = 0
            last_coords = curr
            
        # Choose direction to move
        if x < target_x:
            btn = "Right"
        elif x > target_x:
            btn = "Left"
        elif y < target_y:
            btn = "Down"
        elif y > target_y:
            btn = "Up"
            
        bridge.press_buttons([btn])
        time.sleep(0.4)

# Current: (19, 28)
print("Current position:", bridge.get_coordinates())

# Waypoints to bush
waypoints1 = [
    (24, 28),
    (24, 21),
    (22, 21),
    (22, 14),
    (26, 14)
]

success = True
for wx, wy in waypoints1:
    if not walk_to_waypoint(wx, wy):
        success = False
        break

if success:
    cut_bush()
    
    # Waypoints to Gatehouse
    waypoints2 = [
        (26, 9),
        (37, 9),
        (37, 2),
        (22, 2),
        (22, 4),
        (18, 4),
        (18, 3) # enters Gatehouse
    ]
    
    for wx, wy in waypoints2:
        if not walk_to_waypoint(wx, wy):
            success = False
            break

if success:
    print("Reached inside the Gatehouse! Moving to clerk...")
    # Stand at (2, 4) facing left
    walk_to_waypoint(3, 5)
    walk_to_waypoint(3, 4)
    walk_to_waypoint(2, 4)
    bridge.press_buttons(["Left"])
    time.sleep(0.4)
    
    # Talk to clerk and pay 500
    print("Paying 500 pokedollars...")
    bridge.press_buttons(["A"])
    time.sleep(0.8)
    bridge.press_buttons(["A"]) # YES
    time.sleep(0.8)
    for _ in range(6):
        bridge.press_buttons(["A"])
        time.sleep(0.8)
        
    # Walk UP to row 0 to trigger welcome warp
    print("Walking UP to warp...")
    for _ in range(4):
        bridge.press_buttons(["Up"])
        time.sleep(0.4)
        
    # Clear welcome warp dialogue (mash A until coordinates change from Gatehouse to Safari Center (15, 25))
    print("Clearing welcome dialogue...")
    while True:
        curr = bridge.get_coordinates()
        if curr != (2, 2) and curr != (3, 2) and curr != (4, 2) and curr is not None:
            # We warped!
            if curr[0] == 15 and curr[1] == 25:
                print("Successfully entered Safari Zone Center! Current position:", curr)
                break
        bridge.press_buttons(["A"])
        time.sleep(0.8)
else:
    print("Failed journey to Gatehouse.")
