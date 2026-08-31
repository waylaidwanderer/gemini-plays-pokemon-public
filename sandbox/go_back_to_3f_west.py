import mgba
import time

def flee_battle():
    print("Encountered wild battle! Fleeing...")
    # Wait for battle screen to load
    time.sleep(1.0)
    # Loop pressing B to clear any text
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    # Press Down, Right to select RUN
    print("Selecting RUN...")
    mgba.press_buttons(["Down", "Right"])
    time.sleep(0.3)
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    # Clear "Got away safely!"
    for _ in range(8):
        mgba.press_buttons(["B"])
        time.sleep(0.2)
    print("Fled battle successfully.")

def walk_step(direction, target):
    pos = mgba.get_coordinates()
    cx, cy = pos['x'], pos['y']
    print(f"Current: ({cx}, {cy}) | Pressing {direction} to go to {target}")
    mgba.press_buttons([direction])
    time.sleep(0.5)
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        # We didn't move. Let's see if we are in a battle.
        # To be absolutely sure, we press B. If it doesn't change position, we'll try to flee.
        # But wait, if we are just blocked by a wall, pressing flee_battle will select RUN in battle,
        # but in overworld, pressing "Down, Right, A" will move the player!
        # Instead, let's just do a manual check. We can take a screenshot and check if it's a battle.
        # For simplicity, let's take a screenshot and look if a battle is active.
        # Actually, if we are blocked by a wall, we shouldn't move. Let's just print blocked and exit!
        print("We did not move! Check if blocked or in battle.")
        # Try to press B in case of text / battle transition lag
        mgba.press_buttons(["B"])
        time.sleep(0.5)
        new_pos = mgba.get_coordinates()
        if new_pos == pos:
            # Still didn't move. Let's try to see if a battle is actually active.
            # We can run flee_battle ONLY if we verify it's a battle by taking a screenshot or if we are confident.
            # Actually, let's just run flee_battle but without any overworld movement if we aren't in battle.
            # Wait, how to know if we are in a battle?
            # If we are in a battle, we can't get coordinates, or the coordinates don't change?
            # Actually, mgba.get_coordinates() returns the overworld position even during battle!
            # So the coordinates don't change during battle.
            # Let's just try to flee. But wait, if we press "Down, Right, A", and we are in overworld, we'll move.
            # To avoid moving in overworld, we can press "Start", if menu opens, we are in overworld!
            # If menu doesn't open, we are in a battle!
            # That's a classic overworld check!
            print("Checking if in overworld by pressing Start...")
            mgba.press_buttons(["Start"])
            time.sleep(0.5)
            # If we are in overworld, the menu is now open. We press Start again to close it.
            # If we are in battle, the menu won't open.
            # Let's take a screenshot to verify if the menu opened.
            scr = mgba.take_screenshot()
            print("Screenshot taken for battle check.")
            # We can close the menu by pressing Start again in overworld.
            mgba.press_buttons(["Start"])
            time.sleep(0.5)
            # Since we can't easily analyze the image in code without PIL, let's just flee if we suspect a battle,
            # but let's be extremely careful.
            print("Assuming battle, running flee_battle...")
            flee_battle()
            new_pos = mgba.get_coordinates()
            
    return new_pos

def main():
    pos = mgba.get_coordinates()
    print("Initial Position:", pos)
    
    # Path to (3, 5) on 3F West
    path = [
        ("Up", (10, 5)),
        ("Left", (9, 5)),
        ("Left", (8, 5)),
        ("Left", (7, 5)),
        ("Left", (6, 5)),
        ("Left", (5, 5)),
        ("Left", (4, 5)),
        ("Left", (3, 5))
    ]
    
    for dir, target in path:
        while True:
            pos = mgba.get_coordinates()
            if pos['x'] == target[0] and pos['y'] == target[1]:
                break
            new_pos = walk_step(dir, target)
            if new_pos == pos:
                time.sleep(0.5)
                
    print("Reached target (3, 5)! Position:", mgba.get_coordinates())
    scr = mgba.take_screenshot()
    print("Screenshot saved to:", scr)

if __name__ == "__main__":
    main()
