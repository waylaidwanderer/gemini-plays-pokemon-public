import bridge
import time

print("Closing signpost text box...")
bridge.press_buttons(["B"])
time.sleep(1.0)

# Hardcoded steps to safely walk from (27, 28) to (19, 27) Pokemon Center
steps = [
    "Right", "Right", "Right", # To (30, 28)
    "Down", "Down",            # To (30, 30)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", # To (19, 30)
    "Up", "Up", "Up"           # Into Pokemon Center door at (19, 27)
]

print("Walking hardcoded route...")
for btn in steps:
    print(f"Pressing {btn}...")
    bridge.press_buttons([btn])
    time.sleep(0.44)

print("Transition delay...")
time.sleep(1.5)

curr = bridge.get_coordinates()
print("Emerged inside Pokemon Center at:", curr)
