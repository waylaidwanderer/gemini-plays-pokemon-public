import mgba
import time

def handle_battle_and_continue():
    print("Encountered Wild Ponyta! Escaping...")
    # Dismiss 'Wild PONYTA appeared!' text
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    # Dismiss sending out Pokemon text
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    # Select RUN (Down, Right, A)
    print("Moving cursor to RUN and executing...")
    mgba.press_buttons(["Down", "Right", "A"])
    time.sleep(3.0) # wait for escape animation
    
    # Press B to ensure we are cleanly back on overworld
    mgba.press_buttons(["B"])
    time.sleep(0.5)
    
    pos = mgba.get_coordinates()
    print("Position after escape:", pos)
    
    # We should be at (5, 12). Let's walk the rest of the way:
    # Up to (5, 11)
    # Up to (5, 10)
    # Right to (6, 10)
    # Right to (7, 10)
    # Up to warp to 2F
    if pos['x'] == 5 and pos['y'] == 12:
        print("Continuing walk to stairs...")
        path = [
            ("Up", 5, 11),
            ("Up", 5, 10),
            ("Right", 6, 10),
            ("Right", 7, 10)
        ]
        
        for d, tx, ty in path:
            print(f"At {mgba.get_coordinates()}. Moving {d} to ({tx}, {ty})...")
            mgba.press_buttons([d])
            time.sleep(0.4)
            curr = mgba.get_coordinates()
            if curr['x'] != tx or curr['y'] != ty:
                print(f"INTERRUPTED! Got stuck at {curr}")
                mgba.take_screenshot()
                return False
                
        # We are at (7, 10). Step UP to warp
        print("At stairs (7, 10). Stepping UP to warp to 2F...")
        mgba.press_buttons(["Up"])
        time.sleep(2.0) # wait for warp
        
        final_pos = mgba.get_coordinates()
        print("Position after warp attempt:", final_pos)
        mgba.take_screenshot()
        return True
        
    print("Unexpected position after escape.")
    mgba.take_screenshot()
    return False

if __name__ == "__main__":
    handle_battle_and_continue()
