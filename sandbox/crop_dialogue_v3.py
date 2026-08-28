from PIL import Image
import os

files = [
    "screenshot_1787944196964.png",
    "screenshot_1787944198838.png",
    "screenshot_1787944200706.png",
    "screenshot_1787944202576.png",
    "screenshot_1787944204446.png"
]

for idx, f in enumerate(files):
    path = os.path.join("screenshots", f)
    if os.path.exists(path):
        img = Image.open(path)
        img_std = img.resize((160, 144), Image.Resampling.NEAREST)
        dialogue = img_std.crop((8, 112, 152, 144))
        dialogue_large = dialogue.resize((288, 64), Image.Resampling.NEAREST)
        out_name = f"screenshots/cropped_text_screenshot_{idx}.png"
        dialogue_large.save(out_name)
        print(f"Saved {out_name} from {f}")
    else:
        print(f"File {path} does not exist")
