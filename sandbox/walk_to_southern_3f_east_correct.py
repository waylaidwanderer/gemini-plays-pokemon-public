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

def walk_step_safe(direction, target):
    pos = mgba.get_coordinates()
    cx, cy = pos['x'], pos['y']
    print(f"Current: ({cx}, {cy}) | Pressing {direction} to go to {target}")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print("No movement detected. Checking if in battle...")
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            flee_battle_safe()
            new_pos = mgba.get_coordinates()
    return new_pos

def main():
    pos = mgba.get_coordinates()
    print("Initial Position:", pos)
    
    # Correct path directly via Row 6
    path = [
        ("Down", (14, 6)),
        ("Right", (15, 6)),
        ("Right", (16, 6)),
        ("Right", (17, 6)),
        ("Right", (18, 6)),
        ("Right", (19, 6)),
        ("Right", (20, 6)),
        ("Right", (21, 6)),
        # Down Column 21 to Row 12
        ("Down", (21, 7)),
        ("Down", (21, 8)),
        ("Down", (21, 9)),
        ("Down", (21, 10)),
        ("Down", (21, 11)),
        ("Down", (21, 12)),
        # Right Row 12 to Column 25
        ("Right", (22, 12)),
        ("Right", (23, 12)),
        ("Right", (24, 12)),
        ("Right", (25, 12)),
        # Down Column 25 to Row 14
        ("Down", (25, 13)),
        ("Down", (25, 14))
    ]
    
    start_idx = 0
    min_dist = 9999
    for i, (dir, target) in enumerate(path):
        dist = abs(target[0] - pos['x']) + abs(target[1] - pos['y'])
        if dist < min_dist:
            min_dist = dist
            start_idx = i
            
    print(f"Resuming path from index {start_idx} (target: {path[start_idx][1]})")
    
    for idx in range(start_idx, len(path)):
        dir, target = path[idx]
        while True:
            pos = mgba.get_coordinates()
            if pos['x'] == target[0] and pos['y'] == target[1]:
                break
                
            cx, cy = pos['x'], pos['y']
            tx, ty = target
            if abs(tx - cx) + abs(ty - cy) > 2:
                print("WARPED! Map transition/fall detected! New position:", pos)
                return
                
            new_pos = walk_step_safe(dir, target)
            if new_pos == pos:
                time.sleep(0.5)
                
    print("Reached southern half target (25, 14)! Position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
