import mgba
import time

def handle_potential_battle():
    # If a battle starts, spam B, then press Down, Right, A to run
    print("Executing run-from-battle macro...")
    for _ in range(5):
        mgba.press_buttons(["B", "sleep 150"])
    mgba.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 600"])
    for _ in range(3):
        mgba.press_buttons(["B", "sleep 200"])

def walk_step(direction):
    pos = mgba.get_coordinates()
    mgba.press_buttons([direction])
    time.sleep(0.35)
    new_pos = mgba.get_coordinates()
    
    if new_pos == pos:
        # Position did not change! We might be in a wild battle
        print("Position unchanged. Checking for battle and fleeing...")
        handle_potential_battle()
        # Try moving again after fleeing
        mgba.press_buttons([direction])
        time.sleep(0.35)
        new_pos = mgba.get_coordinates()
        
    return new_pos

def run():
    print("--- WALKING EAST CHUNK 1 ---")
    pos = mgba.get_coordinates()
    print("Start position:", pos)
    
    # 1. Walk Right to (1, 17)
    pos = walk_step("Right")
    print("Position:", pos)
    
    # 2. Walk Down 4 steps to (1, 21) (tall grass)
    for i in range(4):
        pos = walk_step("Down")
        print(f"Step {i+1} Down: {pos}")
        
    # 3. Walk Right 12 steps to (13, 21)
    for i in range(12):
        pos = walk_step("Right")
        print(f"Step {i+1} Right: {pos}")
        
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
