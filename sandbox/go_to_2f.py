import mgba
import time

def run_battle_from_pkmn():
    print("Moving cursor to RUN from PKMN position and running...")
    # Cursor is on PKMN (top-right). Down moves to RUN (bottom-right).
    mgba.press_buttons(["Down", "A"])
    time.sleep(3.0) # Wait for escape
    mgba.press_buttons(["B"])
    time.sleep(0.5)

def walk_step(direction, tx, ty):
    pos = mgba.get_coordinates()
    print(f"At {pos}. Moving {direction} to ({tx}, {ty})...")
    mgba.press_buttons([direction])
    time.sleep(0.4)
    new_pos = mgba.get_coordinates()
    
    if new_pos['x'] == tx and new_pos['y'] == ty:
        return True
        
    print("Blocked or in battle! Attempting to escape...")
    # First press A twice to dismiss intro text (in case battle just started)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    # Press B to close submenus, then Down, Right, A to run
    mgba.press_buttons(["B", "sleep 200", "Down", "Right", "A"])
    time.sleep(3.0)
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    # Check if we successfully got back to the overworld
    new_pos = mgba.get_coordinates()
    print("Post-escape position:", new_pos)
    return False

def run_main():
    # 1. First, we are in battle with cursor on PKMN. Escape now!
    run_battle_from_pkmn()
    
    pos = mgba.get_coordinates()
    print("Overworld pos after escape:", pos)
    
    # 2. Walk path to (7, 10) stairs
    path = [
        ("Up", 5, 11),
        ("Up", 5, 10),
        ("Right", 6, 10),
        ("Right", 7, 10)
    ]
    
    idx = 0
    while idx < len(path):
        d, tx, ty = path[idx]
        if walk_step(d, tx, ty):
            idx += 1
        else:
            # We got into a battle. After escape attempt, retry this same step!
            time.sleep(0.5)
            
    # We reached (7, 10). Step UP to warp to 2F!
    print("Arrived at stairs (7, 10). Stepping UP to warp...")
    mgba.press_buttons(["Up"])
    time.sleep(2.0)
    
    final_pos = mgba.get_coordinates()
    print("Warp complete! Position on 2F:", final_pos)
    mgba.take_screenshot()

if __name__ == "__main__":
    run_main()
