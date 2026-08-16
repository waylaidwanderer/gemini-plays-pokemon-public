import bridge
import time

# Walk from (19, 20) to Pokemon Center (19, 27) by bypassing the checkerboard and balcony via Column 13.
steps = [
    "Right", "Right", "Right", # To (22, 20)
    "Up", "Up", "Up", "Up", "Up", "Up", # To (22, 14)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # To (13, 14)
    "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", # To (13, 28)
    "Right", "Right", "Right", "Right", "Right", "Right", # To (19, 28)
    "Up" # Into PC
]

print("Walking safe path via Column 13...")
for btn in steps:
    print(f"Pressing {btn}...")
    bridge.press_buttons([btn])
    time.sleep(0.44)

print("Transition delay...")
time.sleep(1.5)

curr = bridge.get_coordinates()
print("Emerged inside Pokemon Center at:", curr)
