import mgba
import time

def get_pos():
    p = mgba.get_coordinates()
    while p is None:
        time.sleep(0.1)
        p = mgba.get_coordinates()
    return p

def handle_battle():
    # Run from battle if any
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

# Loop until we successfully toggle!
for attempt in range(10):
    print(f"\n--- Toggle Attempt {attempt+1} ---")
    
    # 1. Walk to (1, 11)
    if not step_to_closed_loop(1, 11):
        print("Failed to reach (1, 11), retrying...")
        continue
        
    # 2. Turn Right to face the switch
    print("Facing Right...")
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    
    # 3. Press A to interact
    print("Pressing A to open textbox...")
    mgba.press_buttons(["A"])
    time.sleep(1.5) # Generous sleep to let text load
    
    # 4. Press Up to select YES
    print("Pressing Up to select YES...")
    mgba.press_buttons(["Up"])
    time.sleep(0.5)
    
    # 5. Check if our position changed
    pos_after_up = get_pos()
    print("Position after Up:", pos_after_up)
    
    if pos_after_up == {'x': 1, 'y': 10}:
        print("Toggle failed! We walked Up instead of selecting YES. Retrying...")
        # Clear any dialogue/screens
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        mgba.press_buttons(["B"])
        time.sleep(0.4)
        continue
    elif pos_after_up == {'x': 1, 'y': 11}:
        print("SUCCESS! We are still at (1, 11), meaning the menu was open and we moved cursor to YES.")
        
        # Press A to select YES
        print("Pressing A to confirm YES...")
        mgba.press_buttons(["A"])
        time.sleep(1.5) # Let click text print
        
        # Press B twice to clear
        print("Clearing text box with B...")
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        
        print("Toggle successful! Verification complete.")
        mgba.take_screenshot()
        break
    else:
        print(f"Unexpected position: {pos_after_up}. Retrying...")
        continue
