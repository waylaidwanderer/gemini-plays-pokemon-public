import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting Master B1F Drop Script. Current pos:", get_pos())

def handle_battle():
    print("  Battle/Dialogue detected! Handling...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.2)
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

# Clear any lingering menus
mgba.press_buttons(["B"])
time.sleep(0.3)

# 1. We are at (16, 9) on 2F. Walk to (16, 11)
step_to_closed_loop(16, 11)

# 2. Warp UP to 3F. Step Left onto stairs at (15, 11).
print("Stepping Left onto stairs at (15, 11) to warp to 3F...")
mgba.press_buttons(["Left"])
time.sleep(2.0)
print("Warp complete. Position on 3F:", get_pos())

# 3. On 3F (State A), walk to the west-side switch at (2, 12).
# Route: (16, 11) -> (18, 11) -> (18, 7) -> (12, 7) -> (12, 11) -> (2, 11) -> (2, 12)
waypoints_3f_state_a = [
    (18, 11),
    (18, 7),
    (12, 7),
    (12, 11),
    (2, 11),
    (2, 12)
]

for (wx, wy) in waypoints_3f_state_a:
    step_to_closed_loop(wx, wy)

# 4. Stand at (2, 12) facing Up and toggle 3F switch to State B!
print("At 3F switch station (2, 12). Facing Up...")
mgba.press_buttons(["Up"])
time.sleep(0.4)

print("Toggling 3F switch to State B...")
mgba.press_buttons([
    "A", "sleep 1000",
    "A", "sleep 1000",
    "Up", "sleep 500",
    "A", "sleep 1000",
    "B", "sleep 500",
    "B"
])
time.sleep(3.0)

# 5. On 3F (State B), walk to the balcony drop landing at (20, 15).
# Route: (2, 12) -> (7, 12) -> (7, 13) -> (9, 13) -> (9, 10) -> (12, 10) -> (12, 5) -> (20, 5) -> (20, 3) -> (26, 3) -> (26, 5) -> (24, 5) -> (24, 7) -> (26, 7) -> (26, 12) -> (25, 12) -> (25, 14) -> (22, 14) -> (21, 14) -> (21, 15) -> (20, 15).
waypoints_3f_state_b = [
    (7, 12),
    (7, 13),
    (9, 13),
    (9, 10),
    (12, 10),
    (12, 5),
    (20, 5),
    (20, 3),
    (26, 3),
    (26, 5),
    (24, 5),
    (24, 7),
    (26, 7),
    (26, 12),
    (25, 12),
    (25, 14),
    (22, 14),
    (21, 14),
    (21, 15),
    (20, 15)
]

for (wx, wy) in waypoints_3f_state_b:
    step_to_closed_loop(wx, wy)

# 6. Drop to B1F!
print("Successfully reached balcony landing (20, 15) on 3F in State B! Dropping...")
mgba.press_buttons([
    "Down", "sleep 400",
    "Down", "sleep 400",
    "Down", "sleep 400",
    "Left"
])
time.sleep(3.0)

print("Master run complete. Landing position on B1F:", get_pos())
mgba.take_screenshot()
