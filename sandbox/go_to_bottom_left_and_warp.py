import mgba
import time

def move(buttons):
    mgba.press_buttons(buttons)
    pos = mgba.get_coordinates()
    print(f"Pressed {buttons}, coordinates: {pos}")
    return pos

print("Starting final B2F navigation to B3F...")

# Step 1: Walk to (14, 22)
move(["Right", "Right", "Right", "Down", "Down"])

# Step 2: Step Left onto (13, 22) LEFT spinner -> slides to (9, 24) stopper
move(["Left", "sleep 3000"])

# Step 3: Walk Left to (8, 24)
move(["Left"])

# Step 4: Step Up onto (8, 23) UP spinner -> slides to (2, 19) stopper
move(["Up", "sleep 3000"])

# Step 5: Walk to (3, 14)
move(["Left"])
move(["Up", "Up", "Up", "Up"])
move(["Right", "Right"])
move(["Up"])

# Step 6: Step Right onto (4, 14) DOWN spinner -> slides Down onto (4, 15) stairs and warps to B3F!
print("Stepping onto (4, 14) DOWN spinner to warp...")
move(["Right", "sleep 3500"])

final_pos = mgba.get_coordinates()
print("Final checked position:", final_pos)
