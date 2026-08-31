import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.2)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.1)
    print("Fled battle safely.")

def walk_to_target(target):
    pos = mgba.get_coordinates()
    if pos['x'] == target[0] and pos['y'] == target[1]:
        print("Already at target.")
        return
        
    direction = None
    if target[0] > pos['x']: direction = "Right"
    elif target[0] < pos['x']: direction = "Left"
    elif target[1] > pos['y']: direction = "Down"
    elif target[1] < pos['y']: direction = "Up"
    
    if direction:
        print(f"Moving {direction} to target {target}...")
        mgba.press_buttons([direction])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # Check for battle
            print("No movement. Pressing B.")
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                flee_battle_safe()

def main():
    print("Testing (27, 12) as B1F East stairs...")
    pos_before = mgba.get_coordinates()
    walk_to_target((27, 12))
    pos_after = mgba.get_coordinates()
    print("Coordinates after move attempt:", pos_after)
    if abs(pos_after['x'] - pos_before['x']) + abs(pos_after['y'] - pos_before['y']) > 5:
        print("WARPED! B1F East stairs successfully triggered!")
    else:
        print("Did not warp. Testing (28, 12)...")
        walk_to_target((28, 12))
        pos_final = mgba.get_coordinates()
        print("Coordinates after (28, 12) attempt:", pos_final)
        if abs(pos_final['x'] - pos_after['x']) + abs(pos_final['y'] - pos_after['y']) > 5:
            print("WARPED on (28, 12)!")

if __name__ == "__main__":
    main()
