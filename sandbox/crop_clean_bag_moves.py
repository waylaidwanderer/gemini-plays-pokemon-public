from PIL import Image
import os

def crop_and_save_1x(filename, crop_rect, out_name):
    if not os.path.exists(filename):
        print(f"{filename} does not exist!")
        return
    img = Image.open(filename)
    # Resize to 160x144 first to make cropping coordinates match 1x
    img_1x = img.resize((160, 144), Image.Resampling.NEAREST)
    cropped = img_1x.crop(crop_rect)
    # Enlarge 2x for high-quality near-neighbor display
    enlarged = cropped.resize((cropped.width * 2, cropped.height * 2), Image.Resampling.NEAREST)
    enlarged.save(out_name)
    print(f"Saved {out_name}")

# Crop the item list area of the bag: x from 40 to 150, y from 16 to 112
crop_and_save_1x("real_bag_p1.png", (40, 16, 150, 112), "bag_items_cropped.png")
crop_and_save_1x("real_bag_p2.png", (40, 16, 150, 112), "bag_items_cropped2.png")

# Crop the move list area of each party slot:
# In the Stats screen, Page 2 shows the moves.
# The moves are listed in the bottom-left or right?
# In Gen 1 stats page 2, the moves are listed on the left side, from y=56 to y=112, x=8 to x=100
for slot in range(1, 6):
    crop_and_save_1x(f"slot_{slot}_moves.png", (8, 56, 100, 112), f"slot_{slot}_moves_cropped.png")

