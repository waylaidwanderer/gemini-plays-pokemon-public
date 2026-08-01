import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

print("Starting sequence to B3F...")

# Step 1: Walk to (10, 14)
move(["Right", "Right", "Down", "Down", "Down"])

# Step 2: Step onto (11, 14) DOWN spinner -> slides to (15, 18) stopper
move(["Right", "sleep 2000"])

# Step 3: Step Left, Left onto (13, 18) LEFT spinner -> slides to (11, 20) stopper
# Wait! Let's check: (13, 18) LEFT spinner slides to (11, 20) stopper, but we need sleep 3000 to be completely sure.
move(["Left", "Left", "sleep 3000"])

# Step 4: From (11, 20) stopper, walk to (14, 22) and step Left onto (13, 22) LEFT spinner -> slides to (9, 24) stopper
move(["Right", "Right", "Right", "Down", "Down"])
move(["Left", "sleep 3000"])

# Step 5: From (9, 24) stopper, walk Left to (8, 24) and step Up onto (8, 23) UP spinner -> slides to (2, 19) stopper
move(["Left"])
move(["Up", "sleep 3000"])

# Step 6: From (2, 19) stopper, walk to (4, 17)
move(["Left"]) # (1, 19)
move(["Up", "Up"]) # (1, 17)
move(["Right", "Right", "Right"]) # (4, 17)

# Step 7: Step Up onto (4, 16) UP spinner -> slides to (7, 14)
print("Stepping onto (4, 16) UP spinner...")
move(["Up", "sleep 3000"])

# Step 8: Walk Left to (6, 14)
move(["Left"])

# Step 9: Walk Down onto (6, 15) stairs/warp tile to warp to B3F!
print("Warping to B3F...")
move(["Down", "sleep 2500"])

final_pos = mgba.get_coordinates()
print("Final checked position:", final_pos)
