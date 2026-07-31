import mgba

print("--- Starting Master Westbound Highway Probe ---")

pos = mgba.get_coordinates()
print(f"Start pos: {pos}")

# Step 1: Navigate from (23, 14) back to (29, 14) via Row 11
path_to_east_lower = [
    "Left", "Left", "Left", "Left",  # to (19, 14)
    "Up", "Up",                      # to (19, 12)
    "Right", "Up",                   # to (20, 11)
    "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", "Right", # to (29, 11)
    "Down", "Down"                   # to (29, 14)
]

mgba.press_buttons(path_to_east_lower)
pos = mgba.get_coordinates()
print(f"Position after bypassing Col 24 cliff: {pos}")

# Step 2: Walk East to Col 53, then Up to Upper Highway (52, 9)
path_to_upper = []
if pos['x'] < 53:
    for _ in range(53 - pos['x']):
        path_to_upper.append("Right")
if pos['y'] > 9:
    for _ in range(pos['y'] - 9):
        path_to_upper.append("Up")

mgba.press_buttons(path_to_upper)
pos = mgba.get_coordinates()
print(f"Position at Upper Highway: {pos}")

# Step 3: Walk West to Col 25
path_to_col25 = []
if pos['x'] > 25:
    for _ in range(pos['x'] - 25):
        path_to_col25.append("Left")

mgba.press_buttons(path_to_col25)
pos = mgba.get_coordinates()
print(f"Position at Col 25: {pos}")

# Step 4: Step Up through Col 25 gap to Row 3
path_up_row3 = ["Up", "Up", "Up", "Up", "Up", "Up"]
mgba.press_buttons(path_up_row3)
pos = mgba.get_coordinates()
print(f"Position at Row 3 Pass: {pos}")
