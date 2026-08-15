import bridge
import time

print("Starting Safari step depletion script with a 90-button safety limit...")

buttons_pressed = 0
while buttons_pressed < 90:
    pos = bridge.get_coordinates()
    print(f"Current position: {pos}, buttons pressed: {buttons_pressed}")
    if pos is None:
        # We are in a battle or textbox. Let's run from battle or clear text.
        print("Coordinates are None. Handling battle/textbox...")
        # Clear textbox
        for _ in range(5):
            bridge.press_buttons(["B", "sleep 150"])
            buttons_pressed += 1
            if buttons_pressed >= 90: break
        if buttons_pressed >= 90: break
        
        # Try to run
        bridge.press_buttons(["Down", "sleep 150", "Right", "sleep 150", "A", "sleep 1000"])
        buttons_pressed += 3
        if buttons_pressed >= 90: break
        
        # Clear post-flee text
        for _ in range(3):
            bridge.press_buttons(["B", "sleep 150"])
            buttons_pressed += 1
            if buttons_pressed >= 90: break
        continue
        
    x, y = pos
    # Stop if we are no longer in the walking area (meaning we warped out!)
    if x != 19 or y not in [23, 24]:
        print(f"Position shifted to {pos}. Stopping script.")
        break
        
    if y == 24:
        next_step = "Up"
    else:
        next_step = "Down"
        
    # Press the next button
    bridge.press_buttons([next_step, "sleep 150"])
    buttons_pressed += 1
    time.sleep(0.1)

print(f"Script finished. Total buttons pressed: {buttons_pressed}")
