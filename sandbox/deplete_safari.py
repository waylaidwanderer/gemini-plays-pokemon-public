import bridge
import time

print("Starting Safari step depletion script...")

while True:
    pos = bridge.get_coordinates()
    print(f"Current position: {pos}")
    if pos is None:
        time.sleep(1)
        continue
        
    x, y = pos
    # Stop if we are no longer in the walking area
    if x != 19 or y not in [23, 24]:
        print(f"Position shifted to {pos}. Stopping script.")
        break
        
    if y == 24:
        next_step = "Up"
    else:
        next_step = "Down"
        
    # Press the next button
    bridge.press_buttons(next_step)
    
    # Get new position
    new_pos = bridge.get_coordinates()
    if new_pos is None:
        continue
        
    new_x, new_y = new_pos
    if new_x == x and new_y == y:
        print("Detected no movement. Attempting to clear textbox...")
        # Press A, then B, to make sure we clear the text and any potential menus
        bridge.press_buttons(["A", "B"])
        time.sleep(0.5)
        # Check again
        new_pos = bridge.get_coordinates()
        print(f"Position after clearing textbox: {new_pos}")
