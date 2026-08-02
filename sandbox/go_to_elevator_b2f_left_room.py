import time
import mgba

def move(buttons):
    mgba.press_buttons(buttons)
    time.sleep(0.3)
    pos = mgba.get_coordinates()
    print(f"Moved {buttons}, now at: {pos}")
    return pos

# First, press B to close the open Start menu
print("Pressing B to close any open Start menu...")
mgba.press_buttons(['B'])
time.sleep(0.5)

pos = mgba.get_coordinates()
print(f"Current pos: {pos}")

# Currently we are at (10, 12).
# Let's walk UP to (10, 10) (the UP spinner) to slide to B2F Left Room at (2, 9).
if pos['x'] == 10 and pos['y'] == 12:
    pos = move(['Up'])  # (10, 11)
    pos = move(['Up'])  # (10, 10) - triggers slide
    print("Waiting for slide...")
    time.sleep(5.0)
    pos = mgba.get_coordinates()
    print(f"Position after slide: {pos}")

# Now we should be at (2, 9) on B2F (the stairs DOWN to B3F).
if pos['x'] == 2 and pos['y'] == 9:
    print("Taking stairs DOWN to B3F...")
    pos = move(['Down'])  # Take the stairs DOWN
    print("Waiting for B3F transition...")
    time.sleep(2.0)
    print(f"New position on B3F: {mgba.get_coordinates()}")

mgba.take_screenshot()
