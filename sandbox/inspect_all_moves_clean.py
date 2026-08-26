# Let's inspect the cropped moves of Slot 3 (Rattata) and Slot 5 (Nidoran-F)
# to see if they know DIG!
import os
from PIL import Image

def find_text_in_moves(filename, slot_num):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist!")
        return
    img = Image.open(filename)
    # The moves are listed in a box. Let's crop the whole screen 1x and save it
    img_1x = img.resize((160, 144), Image.Resampling.NEAREST)
    img_1x.save(f"clean_slot_{slot_num}_moves.png")
    print(f"Saved clean_slot_{slot_num}_moves.png")

# Let's do it for all slots
for i in range(1, 6):
    find_text_in_moves(f"slot_{i}_moves.png", i)
