import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    time.sleep(1.0)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    print("Pressing Down and Right to select RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
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
            # Check if in battle or blocked
            print("No movement. Pressing B to dismiss potential menu/text.")
            mgba.press_buttons(["B"])
            time.sleep(0.5)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                # Still no movement, try to flee
                flee_battle_safe()
                new_pos = mgba.get_coordinates()
                if new_pos == pos:
                    print("Stuck or unable to move. Exiting.")
                    break

def main():
    # Target path from (12, 3) to the pitfall at (26, 4) on Row 3/Row 4 on Column 26
    path = [
        # Down Column 12 to Row 6
        (12, 4), (12, 5), (12, 6),
        # Right along Row 6 to Column 21
        (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (18, 6), (19, 6), (20, 6), (21, 6),
        # Up Column 21 to Row 3
        (21, 5), (21, 4), (21, 3),
        # Right along Row 3 to Column 26
        (22, 3), (23, 3), (24, 3), (25, 3), (26, 3),
        # Down Column 26 to (26, 4) / (26, 5) / (26, 6) to trigger fall
        (26, 4), (26, 5), (26, 6)
    ]
    
    print("Starting exact path navigation to pitfall...")
    for target in path:
        pos = mgba.get_coordinates()
        # Check if we transitioned maps (fell)
        # 3F East has a map index, but we can also check coordinates.
        # If we fell, we land on 1F East inside the fenced room.
        # Our Y coordinate will change drastically (usually 1F East fencing is at a different location or we fall).
        # On 1F East, coordinates are very different or we are not on 3F.
        # Let's check if the coordinates changed drastically from the expected target.
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist > 5:
            print(f"Position {pos} is far from expected target {target}. We must have fallen!")
            break
            
        walk_to_target(target)
        
    print("Navigation finished. Final position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
