import mgba
import time

def flee_battle_safe():
    print("Fleeing battle...")
    # Since cursor is at ITEM:
    # Press Right to move to RUN
    mgba.press_buttons(["Right"])
    time.sleep(0.5)
    # Press A to select RUN
    mgba.press_buttons(["A"])
    time.sleep(2.0)
    # Press B a few times to clear any text/dialogue
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Fled battle.")

def get_dir(curr, target):
    if target[0] > curr['x']: return "Right"
    if target[0] < curr['x']: return "Left"
    if target[1] > curr['y']: return "Down"
    if target[1] < curr['y']: return "Up"
    return None

def walk_to_target(target):
    while True:
        pos = mgba.get_coordinates()
        if pos['x'] == target[0] and pos['y'] == target[1]:
            print(f"Reached target {target}")
            break
            
        direction = get_dir(pos, target)
        if not direction:
            break
            
        print(f"Current: ({pos['x']}, {pos['y']}) | Moving {direction} to target {target}")
        mgba.press_buttons([direction])
        time.sleep(0.5)
        
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            print("No movement. Pressing B.")
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                # If we hit another battle:
                print("Encountered wild battle during walk!")
                # Cursor starts at FIGHT by default in a new battle
                mgba.press_buttons(["Right", "Down", "A"]) # move to RUN and press A
                time.sleep(2.0)
                for _ in range(8):
                    mgba.press_buttons(["B"])
                    time.sleep(0.1)

def toggle_switch():
    print("Toggling switch to State A...")
    mgba.press_buttons(["Left"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["A"])
    time.sleep(1.2)
    mgba.press_buttons(["B"])
    time.sleep(1.0)
    print("Switch toggled.")

def main():
    # First, flee current battle
    flee_battle_safe()
    
    # Check our coordinates after fleeing
    pos = mgba.get_coordinates()
    print("Coordinates after fleeing:", pos)
    
    # Path to switch (from wherever we are, but let's define the full remaining path)
    path_to_switch = [
        (12, 9), (12, 10), (12, 11),
        (11, 11), (10, 11), (9, 11), (8, 11), (7, 11), (6, 11), (5, 11), (4, 11), (3, 11)
    ]
    
    start_idx = 0
    min_dist = 9999
    for i, target in enumerate(path_to_switch):
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist < min_dist:
            min_dist = dist
            start_idx = i
            
    print(f"Continuing walk to switch from index {start_idx}...")
    for idx in range(start_idx, len(path_to_switch)):
        walk_to_target(path_to_switch[idx])
        
    pos = mgba.get_coordinates()
    if pos['x'] == 3 and pos['y'] == 11:
        toggle_switch()
        print("Mansion toggled to State A successfully!")
    else:
        print("Failed to reach switch.", pos)

if __name__ == "__main__":
    main()
