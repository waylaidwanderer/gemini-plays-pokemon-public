import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

pos = mgba.get_coordinates()
print(f"Starting explore_b2f_down from {pos}")

if pos['x'] == 23 and pos['y'] == 3:
    # Walk Down as far as possible up to Row 14
    for i in range(11):
        next_pos = move(['Down'])
        if next_pos['y'] == pos['y']:
            print("Blocked going Down!")
            break
        pos = next_pos

mgba.take_screenshot()
