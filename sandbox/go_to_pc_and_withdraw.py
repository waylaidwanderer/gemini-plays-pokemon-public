# Smart detoured script that dynamically waits/paces if the NPC is blocking (7, 5), then reaches the PC.
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_step(direction):
    bridge.press_buttons([direction, "sleep 250"])
    return get_pos()

def walk_to(target_x, target_y):
    print(f"Navigating to ({target_x}, {target_y})...")
    stuck_count = 0
    last_pos = None
    
    while True:
        pos = get_pos()
        if pos is None:
            time.sleep(0.5)
            continue
            
        if pos == (target_x, target_y):
            print(f"Arrived at {pos}")
            break
            
        if pos == last_pos:
            stuck_count += 1
            if stuck_count > 4:
                print(f"Stuck at {pos} while trying to reach ({target_x}, {target_y})!")
                return False
        else:
            stuck_count = 0
            last_pos = pos
            
        curr_x, curr_y = pos
        if curr_x < target_x:
            walk_step("Right")
        elif curr_x > target_x:
            walk_step("Left")
        elif curr_y < target_y:
            walk_step("Down")
        elif curr_y > target_y:
            walk_step("Up")
            
    return True

def is_npc_blocking():
    # If we are at (5, 5) and try to walk to (7, 5), let's see if we get stuck or if we can test it.
    # Actually, we can just try to walk to (9, 5).
    # If we get stuck, we walk back to (5, 5), pace to (5, 6) and try again.
    pass

def main():
    print("=== SMART DYNAMIC PATHING TO PC ===")
    pos = get_pos()
    print(f"Starting at {pos}")
    if pos is None:
        return
        
    # We are at (5, 6)
    # Step 1: Walk to (5, 5)
    if not walk_to(5, 5):
        return
        
    # We want to walk to (9, 5). If we get stuck because of NPC at (7, 5),
    # we will walk back to (5, 5), walk to (5, 6), and repeat to let the NPC wander.
    attempts = 0
    while attempts < 15:
        print(f"Attempt {attempts+1} to reach (9, 5)...")
        if walk_to(9, 5):
            print("Successfully bypassed (7, 5)!")
            break
        else:
            # We got stuck! Walk back to (5, 5) and pace to (5, 6) to burn time
            print("Path to (9, 5) is blocked. Pacing to let NPC move...")
            walk_to(5, 5)
            walk_to(5, 6)
            walk_to(5, 5)
            attempts += 1
            time.sleep(1.0)
            
    if attempts >= 15:
        print("Failed to bypass NPC after 15 attempts.")
        return
        
    # Once we are at (9, 5), Koga's plants are behind us, and NPC is behind us or to the left!
    # Let's walk to (13, 5)
    if not walk_to(13, 5):
        return
        
    # Walk to (13, 4)
    if not walk_to(13, 4):
        return
        
    # Face Up
    print("Facing Up to PC...")
    walk_step("Up")
    time.sleep(1.0)
    
    # Interacting with PC
    print("Pressing A to boot PC...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    print("Pressing A to advance boot dialogue...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    print("Selecting ACE's PC...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    print("Selecting WITHDRAW ITEM...")
    bridge.press_buttons(["A", "sleep 1000"])
    
    print("Done! Let's check the screen next turn.")

if __name__ == "__main__":
    main()
