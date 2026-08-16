import bridge
import time

# Walk from (26, 14) to Pokemon Center (19, 27) using a fully verified path.
steps = [
    "Left", "Left",                           # To (24, 14)
    "Down", "Down", "Down", "Down", "Down", "Down", # To (24, 20)
    "Left", "Left", "Left", "Left",             # To (20, 20)
    "Up", "Up", "Up", "Up", "Up", "Up",       # To (20, 14)
    "Left", "Left", "Left", "Left", "Left", "Left", "Left", # To (13, 14)
    "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", "Down", # To (13, 28)
    "Right", "Right", "Right", "Right", "Right", "Right", # To (19, 28)
    "Up" # Into PC door at (19, 27)
]

print("Walking safe path from (26, 14) to Pokemon Center...")
for btn in steps:
    print(f"Pressing {btn}...")
    bridge.press_buttons([btn])
    time.sleep(0.44)

print("Transition delay...")
time.sleep(1.5)

curr = bridge.get_coordinates()
print("Emerged inside Pokemon Center at:", curr)

if curr is not None and curr[0] == 3 and curr[1] == 7:
    # Walk to PC at (13, 4)
    # Inside Pokemon Center: (3, 7) -> (13, 4)
    # Right 10 steps to (13, 7), Up 3 steps to (13, 4)
    pc_steps = [
        "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right",
        "Up", "Up", "Up", "Up" # Face the PC
    ]
    print("Walking to PC...")
    for btn in pc_steps:
        bridge.press_buttons([btn])
        time.sleep(0.44)
        
    print("Opening PC...")
    bridge.press_buttons(["A"])
    time.sleep(1.0)
    
    print("Opening ACE's PC...")
    bridge.press_buttons(["A"])
    time.sleep(1.0)
    
    print("Choosing Withdraw Item...")
    bridge.press_buttons(["A"])
    time.sleep(1.0)
    
    print("PC Withdrawal Screen Open!")
