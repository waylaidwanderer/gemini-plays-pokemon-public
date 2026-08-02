import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Current pos: {pos}")

# Walk Left as far as possible on Row 15
while True:
    next_pos = move(['Left'])
    if next_pos['x'] == pos['x']:
        print("Blocked going Left!")
        break
    pos = next_pos

mgba.take_screenshot()
