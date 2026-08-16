import bridge
import time

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
                print(f"Stuck at {curr} trying to reach ({target_x}, {target_y}). Retrying...")
                bridge.press_buttons(["A", "B"])
                time.sleep(0.5)
                stuck_count = 0
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
        time.sleep(0.44)

print("Exiting BAG and Start Menu...")
bridge.press_buttons(["B"])
time.sleep(1.0)
bridge.press_buttons(["B"])
time.sleep(1.0)

print("Exiting Warden's House...")
walk_to_waypoint(4, 7)
bridge.press_buttons(["Down"])
time.sleep(1.0)

print("Emerged outside Warden's House at:", bridge.get_coordinates())

# Now in Fuchsia City overworld.
# Route to Pokemon Center: (27, 30) -> (19, 30) -> (19, 27)
walk_to_waypoint(27, 30)
walk_to_waypoint(19, 30)
walk_to_waypoint(19, 27)

print("Entering Pokemon Center...")
bridge.press_buttons(["Up"])
time.sleep(1.0)

print("Emerged inside PC at:", bridge.get_coordinates())

# Inside Pokemon Center: (3, 7) -> (13, 4)
walk_to_waypoint(13, 4)

print("Opening PC...")
bridge.press_buttons(["Up"])
time.sleep(0.5)
bridge.press_buttons(["A"])
time.sleep(1.0)

# Inside PC main menu:
# 1. ACE's PC
# 2. PROF. OAK'S PC
# 3. PKMN LINK
# 4. LOG OFF
print("Opening ACE's PC...")
bridge.press_buttons(["A"])
time.sleep(1.0)

# Inside ACE's PC menu:
# 1. WITHDRAW ITEM
# 2. DEPOSIT ITEM
# 3. TOSS ITEM
# 4. LOG OFF
print("Choosing Withdraw Item...")
bridge.press_buttons(["A"])
time.sleep(1.0)

print("PC Withdrawal screen open! Position:", bridge.get_coordinates())
