from PIL import Image
import numpy as np

# Load the cropped image
img = Image.open("screenshots/cropped/player_25_8_down_check.png")
arr = np.array(img)

# Print a 10x10 slice around the center of the bottom tile (which is x=20, y=32 in pixels)
print("Pixel values around center of (19, 25) tile:")
for y in range(28, 40):
    row_str = ""
    for x in range(12, 28):
        # Print R value or average color
        val = arr[y, x]
        if isinstance(val, np.ndarray):
            val = val[0]
        row_str += f"{val:02x} "
    print(row_str)
