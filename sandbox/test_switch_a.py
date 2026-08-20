import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

print("Testing interaction from (2, 12) facing Up...")

def handle_battle():
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)
    mgba.press_buttons(["Down", "sleep 100", "Right", "sleep 100", "A"])
    time.sleep(1.2)
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.05)

def step_to_closed_loop(tx, ty):
    for attempt in range(12):
        c = get_pos()
        if c['x'] == tx and c['y'] == ty:
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
        mgba.press_buttons([btn])
        time.sleep(0.4)
        after = get_pos()
        if after == c:
            handle_battle()
            after_retry = get_pos()
            if after_retry == c:
                return False
    return get_pos() == {'x': tx, 'y': ty}

# Walk to (2, 12)
if step_to_closed_loop(2, 12):
    print("Reached (2, 12). Facing Up...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # Press A
    print("Pressing A...")
    mgba.press_buttons(["A"])
    time.sleep(0.8)
    
    # Take screenshot
    screenshot_file = mgba.take_screenshot()
    print("Screenshot taken after A at (2, 12) facing Up:", screenshot_file)
else:
    print("Failed to reach (2, 12)")
