import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

print("Executing complete B3F descent sequence...")
# Current is (12, 9)

# 1. Walk Right to (13, 9)
move(["Right"])

# 2. Walk Down to (13, 11)
move(["Down", "Down"])

# 3. Step Left onto (12, 11) LEFT spinner -> slides to (10, 11)
move(["Left", "sleep 2500"])

# 4. Walk Down to (10, 12)
move(["Down"])

# 5. Step Down onto (10, 13) RIGHT spinner -> slides to (14, 13)
move(["Down", "sleep 2500"])

# 6. Walk Left to (12, 13)
move(["Left", "Left"])

# 7. Walk Down to (12, 16)
move(["Down", "Down", "Down"])

# 8. Walk Left to Column 9 (9, 16)
move(["Left", "Left", "Left"])

# 9. Walk Down to (9, 18)
move(["Down", "Down"])

# 10. Walk Right to (10, 18)
move(["Right"])

# 11. Step Right onto (11, 18) RIGHT spinner -> slides to (14, 18)
move(["Right", "sleep 2500"])

# 12. Step Right onto (15, 18) DOWN spinner -> slides Down
print("Stepping onto (15, 18) DOWN spinner to slide down...")
move(["Right", "sleep 2500"])

final_pos = mgba.get_coordinates()
print("Final position after sliding down:", final_pos)
screenshot_file = mgba.take_screenshot()
print("Saved screenshot to:", screenshot_file)
