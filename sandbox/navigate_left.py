import mgba

target_x = 29
pos = mgba.get_coordinates()
print(f"Start coordinates: {pos}")

while pos['x'] > target_x:
    print(f"Pressing Left from {pos}...")
    mgba.press_buttons(["Left"])
    new_pos = mgba.get_coordinates()
    if new_pos == pos:
        print(f"Blocked or Battle at {pos}! Stopping.")
        break
    pos = new_pos
    print(f"Moved to: {pos}")

print(f"Script finished. Current position: {pos}")
