from PIL import Image

def crop_text(src_path, dest_path):
    img = Image.open(src_path)
    # The screen is 160x144. The text box is at the bottom.
    # In standard Game Boy resolution, the text box spans roughly y=112 to 144, x=8 to 152.
    # But let's crop the bottom part: x=0 to 160, y=100 to 144.
    img_res = img.resize((160, 144), Image.Resampling.NEAREST)
    cropped = img_res.crop((0, 100, 160, 144))
    cropped.save(dest_path)

crop_text("screenshots/screenshot_1787944707680.png", "screenshots/cropped_text_0.png")
crop_text("screenshots/screenshot_1787944709114.png", "screenshots/cropped_text_1.png")
crop_text("screenshots/screenshot_1787944710580.png", "screenshots/cropped_text_2.png")
crop_text("screenshots/screenshot_1787944712063.png", "screenshots/cropped_text_3.png")
crop_text("screenshots/screenshot_1787944713545.png", "screenshots/cropped_text_4.png")

print("Cropped successfully!")
