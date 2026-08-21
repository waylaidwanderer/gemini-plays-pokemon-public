import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting Master Switch-and-Drop Script. Current pos:", get_pos())

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

# Clear menus
mgba.press_buttons(["B"])
time.sleep(0.3)

# 1. Walk to the switch at (12, 11) on 2F
# We are currently at (22, 7) on 2F (State A)
waypoints_to_switch = [
    (12, 7),
    (12, 11)
]

for (wx, wy) in waypoints_to_switch:
    step_to_closed_loop(wx, wy)

# 2. Toggle switch at (13, 11) to State B
print("Standing at (12, 11) on 2F facing Right towards switch at (13, 11).")
mgba.press_buttons(["Right"])
time.sleep(0.4)

print("Toggling switch to State B...")
mgba.press_buttons([
    "A", "sleep 1000",
    "A", "sleep 1000",
    "Up", "sleep 500",
    "A", "sleep 1000",
    "B", "sleep 500",
    "B"
])
time.sleep(3.0)
print("Switch toggled. Current position on 2F:", get_pos())

# 3. Walk to the stairs landing at (16, 11) on 2F (State B)
# Route: (12, 11) -> (12, 7) -> (18, 7) -> (18, 11) -> (16, 11)
waypoints_2f_state_b = [
    (12, 7),
    (18, 7),
    (18, 11),
    (16, 11)
]

for (wx, wy) in waypoints_2f_state_b:
    step_to_closed_loop(wx, wy)

# 4. Warp back UP to 3F (step Left onto (15, 11))
print("Stepping Left onto stairs at (15, 11) to warp to 3F...")
mgba.press_buttons(["Left"])
time.sleep(2.0)
print("Position after warping back to 3F (should be (16, 11)):", get_pos())

# 5. Walk to balcony landing on 3F (State B)
# Route: (16, 11) -> (18, 11) -> (20, 11) -> (20, 14) -> (21, 14) -> (21, 15) -> (20, 15)
waypoints_3f_state_b = [
    (18, 11),
    (20, 11),
    (20, 14),
    (21, 14),
    (21, 15),
    (20, 15)
]

for (wx, wy) in waypoints_3f_state_b:
    step_to_closed_loop(wx, wy)

# 6. Drop to B1F!
print("Reached balcony landing (20, 15) in State B! Dropping to B1F...")
mgba.press_buttons([
    "Down", "sleep 400",
    "Down", "sleep 400",
    "Down", "sleep 400",
    "Left"
])
time.sleep(3.0)

print("Master run complete. Landing position on B1F:", get_pos())
mgba.take_screenshot()
