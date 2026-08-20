import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Starting Part 2 of master bypass route. Current pos on 3F:", get_pos())

def handle_battle():
    print("Action blocked or battle detected! Running battle auto-pilot...")
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    # Select RUN
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.2)
    # Clear escaping messages
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.1)

def step_to(tx, ty):
    for _ in range(10): # retry loop
        c = get_pos()
        if c['x'] == tx and c['y'] == ty:
            print(f"Reached: ({tx}, {ty})")
            return True
        dx = tx - c['x']
        dy = ty - c['y']
        
        btn = None
        if dx > 0:
            btn = "Right"
        elif dx < 0:
            btn = "Left"
        elif dy > 0:
            btn = "Down"
        elif dy < 0:
            btn = "Up"
            
        print(f"Standing at {c}. Pressing {btn} to reach ({tx}, {ty})...")
        mgba.press_buttons([btn])
        time.sleep(0.4)
        
        after = get_pos()
        if after == c:
            print("Blocked! Checking for battle...")
            handle_battle()
            after_retry = get_pos()
            if after_retry == c:
                print("STILL BLOCKED. Aborting.")
                return False
    return False

# Route steps:
# 1. (1, 11) -> (1, 13)
if not step_to(1, 12): exit(1)
if not step_to(1, 13): exit(1)

# 2. (1, 13) -> (5, 13)
if not step_to(2, 13): exit(1)
if not step_to(3, 13): exit(1)
if not step_to(4, 13): exit(1)
if not step_to(5, 13): exit(1)

# 3. (5, 13) -> (5, 6)
for y in range(12, 5, -1):
    if not step_to(5, y): exit(1)

# 4. (5, 6) -> (16, 6)
for x in range(6, 17):
    if not step_to(x, 6): exit(1)

# 5. (16, 6) -> (16, 11)
for y in range(7, 12):
    if not step_to(16, y): exit(1)

# 6. (16, 11) -> (15, 11) (warps DOWN to 2F)
print("Warping down to 2F east wing...")
mgba.press_buttons(["Left"])
time.sleep(1.5)
print("Final landing pos on 2F:", get_pos())
