import mgba
import time

print("Walking down to row 15 on column 25 to see if there is a way south...")
buttons = []
# We are currently at (25, 2).
# Let's walk Down to (25, 15).
# From y=2 to y=15 is 13 steps Down.
for i in range(13):
    buttons.append("Down")
    buttons.append("sleep 300")

mgba.press_buttons(buttons)
time.sleep(4.0)

pos = mgba.get_coordinates()
print("Position after walking Down:", pos)
mgba.take_screenshot()
