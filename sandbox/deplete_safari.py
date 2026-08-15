import bridge
import time

print("Starting Safari step depletion script at Column 29...")

buttons_pressed = 0
while buttons_pressed < 85:
    pos = bridge.get_coordinates()
    print(f"Current position: {pos}, buttons pressed: {buttons_pressed}")
    if pos is None:
        print("Coordinates are None. Handling battle/textbox...")
        for _ in range(5):
            bridge.press_buttons("B")
            buttons_pressed += 1
            if buttons_pressed >= 85: break
            time.sleep(0.1)
        if buttons_pressed >= 85: break
        
        bridge.press_buttons("Down")
        bridge.press_buttons("Right")
        bridge.press_buttons("A")
        buttons_pressed += 3
        if buttons_pressed >= 85: break
        
        for _ in range(3):
            bridge.press_buttons("B")
            buttons_pressed += 1
            if buttons_pressed >= 85: break
            time.sleep(0.1)
        continue
        
    x, y = pos
    # Stop if we are no longer in the walking area (meaning we warped out!)
    if x not in [28, 29] or y != 23:
        print(f"Position shifted to {pos}. Stopping script.")
        break
        
    if x == 29:
        next_step = "Left"
    else:
        next_step = "Right"
        
    # Press the next button
    bridge.press_buttons(next_step)
    buttons_pressed += 1
    time.sleep(0.3)

print(f"Script finished. Total buttons pressed: {buttons_pressed}")
