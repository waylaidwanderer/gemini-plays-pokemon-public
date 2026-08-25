import mgba
import time

def check_pos():
    pos = mgba.get_coordinates()
    print(f"Position: {pos}")
    return pos

# Currently at (9, 11)
# Walk LEFT along Row 11 to Column 6
print("Walking LEFT to Column 6...")
for x in range(8, 5, -1):
    mgba.press_buttons(["Left"])
    time.sleep(0.4)
    check_pos()

# Walk UP Column 6 as far as we can
print("Walking UP Column 6...")
for i in range(5):
    mgba.press_buttons(["Up"])
    time.sleep(0.4)
    check_pos()
