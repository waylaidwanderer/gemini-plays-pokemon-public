import mgba
import time

def walk_step(direction):
    print(f"Walking {direction}...")
    mgba.press_buttons([direction])
    time.sleep(0.3)  # Allow time for movement animation

def main():
    pos = mgba.get_coordinates()
    print(f"Starting position: {pos}")
    
    # Goal: Reach X=29, Y=10 or 11
    # We are currently at (20, 22)
    # We will try to walk Right to column 29
    # If we hit an obstacle, we will stop and report.
    
    steps = 0
    max_steps = 40
    
    while steps < max_steps:
        pos = mgba.get_coordinates()
        x, y = pos['x'], pos['y']
        print(f"Current Position: ({x}, {y})")
        
        # Check if we transitioned to Area 1 (East)
        # Area 1 (East) is a different map, usually coordinates reset or change,
        # but let's check if X becomes 0 or 1 in Area 1
        if x > 29 or (x == 29 and (y == 10 or y == 11)):
            # Try to walk Right to transition
            walk_step("Right")
            time.sleep(1.0)
            new_pos = mgba.get_coordinates()
            print(f"Transitioned? New Position: {new_pos}")
            break
            
        if x < 29:
            # Move Right
            walk_step("Right")
            time.sleep(0.1)
            new_pos = mgba.get_coordinates()
            if new_pos == pos:
                print("Could not move Right. Obstacle or Battle!")
                break
        elif x == 29:
            if y > 10:
                # Move Up
                walk_step("Up")
                time.sleep(0.1)
                new_pos = mgba.get_coordinates()
                if new_pos == pos:
                    print("Could not move Up. Obstacle or Battle!")
                    break
            elif y < 10:
                # Move Down
                walk_step("Down")
                time.sleep(0.1)
                new_pos = mgba.get_coordinates()
                if new_pos == pos:
                    print("Could not move Down. Obstacle or Battle!")
                    break
        steps += 1

if __name__ == "__main__":
    main()
