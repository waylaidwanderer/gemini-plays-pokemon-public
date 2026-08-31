import mgba
import time

def flee_battle_safe():
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.2)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Fled battle safely.")

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
                # If we hit a wild battle along the way
                print("Wild battle detected along the way!")
                mgba.press_buttons(["Down", "Right"])
                time.sleep(0.2)
                mgba.press_buttons(["A"])
                time.sleep(1.5)
                for _ in range(8):
                    mgba.press_buttons(["B"])
                    time.sleep(0.1)
                time.sleep(0.5)

def main():
    # We are in battle at (4, 2)
    flee_battle_safe()
    
    # Path to switch at (2, 5) standing at (3, 5):
    path = [
        (4, 3), (4, 4), (4, 5), (3, 5)
    ]
    
    print("Starting walk to switch area...")
    for target in path:
        walk_to_target(target)
        
    print("Reached (3, 5). Turning LEFT to face switch at (2, 5)...")
    mgba.press_buttons(["Left"])
    time.sleep(0.8)
    
    # Toggle switch to State A (requires exactly 4 A presses to clear text box)
    print("Toggling switch to State A...")
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(0.5)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Clear residual dialog
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    print("Mansion set to State A. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
