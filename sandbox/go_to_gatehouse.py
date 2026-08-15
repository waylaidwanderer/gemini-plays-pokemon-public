import bridge
import time

def cut_bush():
    print("Cutting bush at (26, 13)...")
    # Face UP towards the bush
    bridge.press_buttons(["Up"])
    time.sleep(0.4)
    
    # Open START menu
    bridge.press_buttons(["Start"])
    time.sleep(0.5)
    
    # Go to POKEMON (Down, A)
    bridge.press_buttons(["Down", "A"])
    time.sleep(0.5)
    
    # Select TRUFFLE (Paras) - press Down once to highlight TRUFFLE, then A
    bridge.press_buttons(["Down", "A"])
    time.sleep(0.5)
    
    # Select CUT (since we are facing a bush, CUT is the top option, so just press A)
    bridge.press_buttons(["A"])
    time.sleep(1.5) # Wait for cut animation
    
    # Clear "TRUFFLE hacked away with CUT!" text
    bridge.press_buttons(["A"])
    time.sleep(0.5)
    print("Bush cut successfully.")

# Walk from (19, 28) to (26, 14)
print("Current position:", bridge.get_coordinates())

steps1 = [
    ("Right", (20, 28)),
    ("Right", (21, 28)),
    ("Right", (22, 28)),
    ("Right", (23, 28)),
    ("Right", (24, 28)),
    ("Up", (24, 27)),
    ("Up", (24, 26)),
    ("Up", (24, 25)),
    ("Up", (24, 24)),
    ("Up", (24, 23)),
    ("Up", (24, 22)),
    ("Up", (24, 21)),
    ("Left", (23, 21)),
    ("Left", (22, 21)),
    ("Up", (22, 20)),
    ("Up", (22, 19)),
    ("Up", (22, 18)),
    ("Up", (22, 17)),
    ("Up", (22, 16)),
    ("Up", (22, 15)),
    ("Up", (22, 14)),
    ("Right", (23, 14)),
    ("Right", (24, 14)),
    ("Right", (25, 14)),
    ("Right", (26, 14))
]

def walk_steps(steps):
    for button, expected in steps:
        curr = bridge.get_coordinates()
        bridge.press_buttons([button])
        time.sleep(0.4)
        new_coords = bridge.get_coordinates()
        if new_coords != expected:
            print(f"Failed to reach {expected}. Ended up at {new_coords} from {curr} via {button}")
            return False
    return True

if walk_steps(steps1):
    cut_bush()
    
    # Walk from (26, 14) through the cut bush to the Gatehouse entrance at (18, 3)
    steps2 = [
        ("Up", (26, 13)), # through cut bush
        ("Up", (26, 12)),
        ("Up", (26, 11)),
        ("Up", (26, 10)),
        ("Up", (26, 9)),
        ("Left", (25, 9)),
        ("Left", (24, 9)),
        ("Left", (23, 9)),
        ("Left", (22, 9)),
        ("Left", (21, 9)),
        ("Left", (20, 9)),
        ("Left", (19, 9)),
        ("Up", (19, 8)),
        ("Right", (20, 8)),
        ("Right", (21, 8)),
        ("Right", (22, 8)),
        ("Right", (23, 8)),
        ("Right", (24, 8)),
        ("Right", (25, 8)),
        ("Right", (26, 8)),
        ("Right", (27, 8)),
        ("Right", (28, 8)),
        ("Right", (29, 8)),
        ("Right", (30, 8)),
        ("Right", (31, 8)),
        ("Right", (32, 8)),
        ("Right", (33, 8)),
        ("Right", (34, 8)),
        ("Right", (35, 8)),
        ("Right", (36, 8)),
        ("Right", (37, 8)),
        ("Up", (37, 7)),
        ("Up", (37, 6)),
        ("Up", (37, 5)),
        ("Up", (37, 4)),
        ("Up", (37, 3)),
        ("Up", (37, 2)),
        ("Left", (36, 2)),
        ("Left", (35, 2)),
        ("Left", (34, 2)),
        ("Left", (33, 2)),
        ("Left", (32, 2)),
        ("Left", (31, 2)),
        ("Left", (30, 2)),
        ("Left", (29, 2)),
        ("Left", (28, 2)),
        ("Left", (27, 2)),
        ("Left", (26, 2)),
        ("Left", (25, 2)),
        ("Left", (24, 2)),
        ("Left", (23, 2)),
        ("Left", (22, 2)),
        ("Down", (22, 3)),
        ("Down", (22, 4)),
        ("Left", (21, 4)),
        ("Left", (20, 4)),
        ("Left", (19, 4)),
        ("Left", (18, 4)),
        ("Up", (18, 3)) # enters Gatehouse!
    ]
    
    if walk_steps(steps2):
        print("Successfully reached inside the Safari Gatehouse!")
    else:
        print("Failed steps2. Current:", bridge.get_coordinates())
else:
    print("Failed steps1. Current:", bridge.get_coordinates())
