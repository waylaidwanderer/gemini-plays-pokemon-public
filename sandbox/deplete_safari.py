import bridge
import time

print("Starting Safari step depletion script with maximum efficiency...")

buttons_pressed = 0
while buttons_pressed < 85:
    pos = bridge.get_coordinates()
    print(f"Current position: {pos}, buttons pressed: {buttons_pressed}")
    if pos is None:
        # We are in a battle or textbox. Let's run from battle or clear text.
        print("Coordinates are None. Handling battle/textbox...")
        # Clear textbox
        for _ in range(5):
            bridge.press_buttons("B")
            buttons_pressed += 1
            if buttons_pressed >= 85: break
            time.sleep(0.1)
        if buttons_pressed >= 85: break
        
        # Try to run
        bridge.press_buttons("Down")
        bridge.press_buttons("Right")
        bridge.press_buttons("A")
        buttons_pressed += 3
        if buttons_pressed >= 85: break
        
        # Clear post-flee text
        for _ in range(3):
            bridge.press_buttons("B")
            buttons_pressed += 1
            if buttons_pressed >= 85: break
            time.sleep(0.1)
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
    bridge.press_buttons(next_step)
    buttons_pressed += 1
    time.sleep(0.3)

print(f"Script finished. Total buttons pressed: {buttons_pressed}")
