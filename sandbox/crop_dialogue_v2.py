from PIL import Image
import os

img = Image.open("screenshots/screenshot_1787940922022.png")
img_std = img.resize((160, 144), Image.Resampling.NEAREST)
dialogue = img_std.crop((8, 112, 152, 144))
dialogue_large = dialogue.resize((288, 64), Image.Resampling.NEAREST)
dialogue_large.save("screenshots/cropped_text_screenshot_1787940922022.png")
print("Saved!")
