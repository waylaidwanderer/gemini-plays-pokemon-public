import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting at: {pos}")

# Currently at (21, 15) on B2F
# Walk Up Column 21 to Row 8 stairs (7 steps Up)
print("Walking Up Column 21 to reach B3F stairs...")
for _ in range(7):
    pos = move(["Up"])

print("Final position after warp attempt:", mgba.get_coordinates())
mgba.take_screenshot()
