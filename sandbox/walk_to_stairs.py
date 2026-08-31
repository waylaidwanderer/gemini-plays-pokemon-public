import mgba
import time

def flee_battle():
    print("Wild battle detected! Fleeing...")
    # Press B a few times to clear text
    for _ in range(5):
        mgba.press_buttons(["B"])
        time.sleep(0.3)
    # Select RUN (Down, Right, A)
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(1.0)
    # Clear "Got away safely!"
    for _ in range(4):
        mgba.press_buttons(["B"])
        time.sleep(0.3)

def walk_to(target_x, target_y):
    stuck_count = 0
    last_pos = None
    
    while True:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        print(f"Current Position: ({x}, {y})")
        
        if x == target_x and y == target_y:
            print("Arrived at target!")
            break
            
        if last_pos == (x, y):
            stuck_count += 1
            if stuck_count > 3:
                print("Stuck! Attempting to flee battle or recover...")
                flee_battle()
                stuck_count = 0
                continue
        else:
            stuck_count = 0
            last_pos = (x, y)
            
        # Determine next step
        buttons = []
        if x > target_x:
            buttons.append("Left")
        elif x < target_x:
            buttons.append("Right")
        elif y > target_y:
            buttons.append("Up")
        elif y < target_y:
            buttons.append("Down")
            
        if buttons:
            mgba.press_buttons(buttons)
            time.sleep(0.3)

print("Starting walk from (12, 2) to (5, 11)...")
walk_to(5, 11)
# Step onto the stairs warp tile once more to ensure warp triggers
print("Arrived at 2F West stairs (5, 11). Activating warp...")
mgba.press_buttons(["Down"]) # Step into the stairs
time.sleep(1.5)
