from PIL import Image

# Read and check the screenshot from Turn 70473
# The player was at (21, 16) on 3F East in State B.
# We will crop the area around (21, 17) to verify if the gate is open or closed in State B.
# In a 480x432 image, each tile is 16x16? Let's check.
# Game Boy screen is 160x144, but the screenshot is 480x432 which is exactly 3x scale.
# In 3x scale, each 8x8 tile is 24x24 pixels, and 16x16 tile is 48x48 pixels.
# Let's write a script to save crops of key areas from this screenshot.

img = Image.open("screenshots/screenshot_1788214373540.png")

# Let's crop the bottom half of the screen where the gate at (21, 17) would be.
# Since the player is at (21, 16) and is shown near the center of the screen,
# (21, 17) is directly below the player.
# Let's crop a region below the player.
# In a 160x144 screen (3x scaled to 480x432):
# Player is usually at the center: X_center = 240, Y_center = 216.
# Directly below the player (one 16x16 tile below) is at Y_center + 48 = 264.
# Let's crop a 120x120 area centered below the player.
crop_gate = img.crop((180, 216, 300, 336))
crop_gate.save("screenshots/cropped/balcony_gate_state_b.png")
print("Saved crop to screenshots/cropped/balcony_gate_state_b.png")
