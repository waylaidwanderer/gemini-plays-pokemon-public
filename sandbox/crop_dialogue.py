from PIL import Image
import os

files = [
    "screenshot_1787940321891.png",
    "screenshot_1787940323381.png",
    "screenshot_1787940324883.png",
    "screenshot_1787940326134.png"
]

for idx, f in enumerate(files):
    path = os.path.join("screenshots", f)
    if os.path.exists(path):
        img = Image.open(path)
        # Resize to standard Gameboy size 160x144 if it isn't already
        img_std = img.resize((160, 144), Image.Resampling.NEAREST)
        # Crop dialogue box area: x in [8, 152], y in [112, 144]
        # Since crop takes box (left, upper, right, lower)
        # Let's upscale it by 2x for readability
        dialogue = img_std.crop((8, 112, 152, 144))
        dialogue_large = dialogue.resize((288, 64), Image.Resampling.NEAREST)
        out_name = f"screenshots/cropped_text_{idx}.png"
        dialogue_large.save(out_name)
        print(f"Saved {out_name}")
    else:
        print(f"File {path} does not exist")
