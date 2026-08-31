import mgba
import time

def flee_battle_safe():
    print("Wild battle detected! Fleeing safely...")
    # Wait for battle screen to load
    time.sleep(1.0)
    # Clear any text by pressing B
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    # Select RUN
    print("Pressing Down and Right to select RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.3)
    # Press A to execute RUN
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    # Clear "Got away safely!" by pressing B
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
        # We didn't move. This could be due to a battle or a physical wall.
        # Let's try pressing B to check if we are in battle.
        print("No movement detected. Checking if in battle...")
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # We still didn't move. Let's try to flee battle but without pressing overworld directions!
            # To avoid moving the player if we are in overworld, we can press Start to check overworld.
            # But let's just attempt a safe flee: if we are in battle, the cursor will move to RUN and we will flee.
            # If we are in overworld, pressing B, Down, Right, A might open and close the menu or do nothing.
            # Actually, to be completely safe, we can just run the flee battle routine.
            flee_battle_safe()
            new_pos = mgba.get_coordinates()
    return new_pos

def main():
    pos = mgba.get_coordinates()
    print("Initial Position:", pos)
    
    # Correct path to the southern half of 3F East via Row 2 and Column 21
    path = [
        # From (4, 5) to (10, 5)
        ("Right", (5, 5)),
        ("Right", (6, 5)),
        ("Right", (7, 5)),
        ("Right", (8, 5)),
        ("Right", (9, 5)),
        ("Right", (10, 5)),
        # Up Column 10 to Row 2
        ("Up", (10, 4)),
        ("Up", (10, 3)),
        ("Up", (10, 2)),
        # Right Row 2 to Column 21
        ("Right", (11, 2)),
        ("Right", (12, 2)),
        ("Right", (13, 2)),
        ("Right", (14, 2)),
        ("Right", (15, 2)),
        ("Right", (16, 2)),
        ("Right", (17, 2)),
        ("Right", (18, 2)),
        ("Right", (19, 2)),
        ("Right", (20, 2)),
        ("Right", (21, 2)),
        # Down Column 21 to Row 12
        ("Down", (21, 3)),
        ("Down", (21, 4)),
        ("Down", (21, 5)),
        ("Down", (21, 6)),
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
    
    # Find our current position in the path to support resume
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
                
            # If coordinates changed drastically, we fell through the pitfall!
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
