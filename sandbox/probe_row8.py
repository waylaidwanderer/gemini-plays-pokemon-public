import mgba

print("Starting Row 8 Westbound single-step collision probe...")
start_pos = mgba.get_coordinates()
print(f"Start Position: {start_pos}")

for step in range(1, 40):
    mgba.press_buttons(["Left"])
    curr_pos = mgba.get_coordinates()
    print(f"Step {step}: {curr_pos}")
    if curr_pos['x'] == start_pos['x'] and curr_pos['y'] == start_pos['y']:
        print(f"COLLISION DETECTED at step {step}! Position remained {curr_pos}")
        screenshot = mgba.take_screenshot()
        print(f"Screenshot saved: {screenshot}")
        break
    start_pos = curr_pos
    if curr_pos['x'] <= 23:
        print(f"SUCCESS! Reached Column {curr_pos['x']} at (x={curr_pos['x']}, y={curr_pos['y']})!")
        break
