import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting Alternate Balcony Route Script. Current pos:", get_pos())

def handle_battle():
    print("  Battle/Dialogue detected! Handling...")
    # Clear screens
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    # Run from battle
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.2)
    # Clear textbox
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)

def step_to_closed_loop(tx, ty):
    print(f"Navigating to ({tx}, {ty})...")
    for attempt in range(15):
        c = get_pos()
        if c['x'] == tx and c['y'] == ty:
            print(f"Reached: ({tx}, {ty})")
            return True
            
        dx = tx - c['x']
        dy = ty - c['y']
        
        btn = None
        if abs(dx) >= abs(dy):
            if dx > 0: btn = "Right"
            else: btn = "Left"
        else:
            if dy > 0: btn = "Down"
            else: btn = "Up"
            
        print(f"  Attempt {attempt+1}/15. Pos: {c}. Pressing {btn}")
        mgba.press_buttons([btn])
        time.sleep(0.4)
        
        after = get_pos()
        if after == c:
            print("  Blocked! Checking for battle/dialogue...")
            handle_battle()
            after_retry = get_pos()
            print(f"  After retry, pos is: {after_retry}")
            
    c_final = get_pos()
    if c_final['x'] == tx and c_final['y'] == ty:
        return True
    return False

# We are at (16, 9) on 3F.
# 1. Walk to stairs landing at (16, 11) on 3F.
step_to_closed_loop(16, 11)

# 2. Warp DOWN to 2F.
# Since stairs are at (15, 11), we step Left.
print("Stepping Left onto stairs at (15, 11) to warp to 2F...")
mgba.press_buttons(["Left"])
time.sleep(2.0)
print("Position after 2F warp attempt:", get_pos())

# 3. We are now on 2F. Walk to the switch at (12, 11) on 2F.
# Waypoints on 2F (State A): (16, 11) -> (16, 7) -> (12, 7) -> (12, 11).
waypoints_to_switch = [
    (16, 7),
    (12, 7),
    (12, 11)
]

for (wx, wy) in waypoints_to_switch:
    step_to_closed_loop(wx, wy)

# 4. Turn Right and toggle the 2F switch to State B!
print("Standing at (12, 11) on 2F facing the statue at (13, 11). Turning Right...")
mgba.press_buttons(["Right"])
time.sleep(0.4)

print("Toggling 2F switch...")
mgba.press_buttons([
    "A", "sleep 1000",
    "A", "sleep 1000",
    "Up", "sleep 500",
    "A", "sleep 1000",
    "B", "sleep 500",
    "B"
])
time.sleep(3.0)

# 5. Walk back to the stairs landing at (16, 11) on 2F (State B).
# Waypoints on 2F (State B): (12, 11) -> (12, 7) -> (16, 7) -> (16, 11).
waypoints_back = [
    (12, 7),
    (16, 7),
    (16, 11)
]

for (wx, wy) in waypoints_back:
    step_to_closed_loop(wx, wy)

# 6. Warp back UP to 3F.
print("Stepping Left onto stairs at (15, 11) to warp back to 3F...")
mgba.press_buttons(["Left"])
time.sleep(2.0)
print("Position after 3F warp attempt:", get_pos())

# 7. We are now on 3F in State B. Walk to the balcony drop landing at (20, 15).
# Waypoints on 3F (State B): (16, 11) -> (18, 11) -> (18, 14) -> (20, 14) -> (20, 15).
waypoints_to_balcony = [
    (18, 11),
    (18, 14),
    (20, 14),
    (20, 15)
]

for (wx, wy) in waypoints_to_balcony:
    step_to_closed_loop(wx, wy)

# 8. Drop to B1F!
# Walk Down through the open gate at (20, 17) to (20, 18), then step Left to (19, 18) to drop!
print("At balcony landing (20, 15). Walking down to drop...")
mgba.press_buttons([
    "Down", "sleep 400",
    "Down", "sleep 400",
    "Down", "sleep 400",
    "Left"
])
time.sleep(3.0)

print("Final position after dropping:", get_pos())
mgba.take_screenshot()
