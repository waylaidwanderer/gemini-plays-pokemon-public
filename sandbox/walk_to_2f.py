import mgba
import time

def run_from_battle():
    print("Battle detected! Running away...")
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    mgba.press_buttons(["Right", "sleep 100", "Down", "sleep 100", "A", "sleep 2000"])
    mgba.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    time.sleep(1.0)

print("Walking UP column 5 from (5, 27) to (5, 10) stairs...")

current_y = 27
target_y = 10

while current_y > target_y:
    pos = mgba.get_coordinates()
    print(f"Current Position: {pos}, Next: Up to column 5, row {current_y - 1}")
    
    mgba.press_buttons(["Up"])
    time.sleep(0.3)
    
    new_pos = mgba.get_coordinates()
    if new_pos['y'] < pos['y'] and new_pos['x'] == 5:
        print("Step succeeded.")
        current_y = new_pos['y']
    else:
        # Check if we transitioned to 2F (which would change map or warp us)
        # Note: stepping onto (5, 10) warps us to 2F.
        # On 2F, the corresponding stairs warp is usually at (5, 10) or similar.
        # Let's check if we warped.
        if new_pos['y'] == 10:
            # Check if we are still on 1F or already on 2F
            # Let's take a screenshot and check
            print("Reached (5, 10)!")
            break
            
        print("Failed to step up. Checking for battle or blockage...")
        time.sleep(0.5)
        pos_check = mgba.get_coordinates()
        if pos_check == new_pos:
            # We are stuck/blocked or in a battle
            # Let's run run_from_battle
            run_from_battle()
            time.sleep(1.0)
            new_pos_after = mgba.get_coordinates()
            current_y = new_pos_after['y']
        else:
            print("Position changed, updating current_y...")
            current_y = new_pos['y']

# If we reached (5, 10) on 1F, we need to take one more step onto the stairs at (5, 10)?
# Wait, in walk_to_b1f_stairs_1f.py, the stairs warp is at (5, 10).
# Let's check coordinates after the loop.
final_pos = mgba.get_coordinates()
print("Final Position:", final_pos)
mgba.take_screenshot()
