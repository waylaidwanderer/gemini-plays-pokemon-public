from PIL import Image
import os

os.makedirs("screenshots/cropped", exist_ok=True)

# Crop region for the moves list on Stats Page 2
# x from 72 to 160, y from 16 to 112
# On 480x432 scale (3x): x from 216 to 480, y from 48 to 336
box = (200, 30, 480, 360)

slots_moves = [
    "screenshot_1787708703599.png", # Slot 1 Moves
    "screenshot_1787708709915.png", # Slot 2 Moves
    "screenshot_1787708716235.png", # Slot 3 Moves
    "screenshot_1787708722562.png", # Slot 4 Moves
    "screenshot_1787708728871.png", # Slot 5 Moves
    "screenshot_1787708735193.png"  # Slot 6 Moves
]

for idx, f in enumerate(slots_moves):
    p = os.path.join("screenshots", f)
    if os.path.exists(p):
        img = Image.open(p)
        cropped_img = img.crop(box)
        cropped_p = f"screenshots/cropped/slot_{idx+1}_moves.png"
        cropped_img.save(cropped_p)
        print(f"Saved cropped Slot {idx+1} Moves to {cropped_p}")
