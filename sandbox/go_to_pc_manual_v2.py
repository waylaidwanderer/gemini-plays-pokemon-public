import bridge
import time

# Safely walk from (24, 27) to Pokemon Center (19, 27) by going North to Row 20, crossing West, and going South.
steps = [
    "Up", "Up", "Up", "Up", "Up", "Up", "Up", # To (24, 20)
    "Left", "Left",                           # To (22, 20)
    "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", # To (22, 28)
    "Left", "Left", "Left",                   # To (19, 28)
    "Up"                                      # Into PC door
]

print("Walking safe path via Row 20...")
for btn in steps:
    print(f"Pressing {btn}...")
    bridge.press_buttons([btn])
    time.sleep(0.44)

print("Transition delay...")
time.sleep(1.5)

curr = bridge.get_coordinates()
print("Emerged inside Pokemon Center at:", curr)
