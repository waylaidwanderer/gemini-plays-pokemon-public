from PIL import Image
import os

def find_player_sprite(img_path):
    img = Image.open(img_path)
    # The clean Game Boy screen is 160x144. Our screenshot size is 480x432, which is exactly a 3x scale of 160x144!
    # So each pixel in 160x144 is represented by a 3x3 pixel block in 480x432.
    # Let's resize the image down to 160x144 using nearest-neighbor to get the original 160x144 pixel clean screen!
    img_160 = img.resize((160, 144), Image.Resampling.NEAREST)
    
    # The player character's red cap has a very specific bright red color.
    # In RGB (under GBC filter), let's find the most common reddish pixels.
    # In standard Pokémon Red/Blue, the red cap has a distinct palette color.
    # Let's scan all pixels and print the coordinates of red/pink/orange pixels to find the player cap!
    red_pixels = []
    for y in range(144):
        for x in range(160):
            r, g, b = img_160.getpixel((x, y))[:3]
            # Red cap color is usually bright red/orange (high R, lower G and B)
            if r > 180 and g < 100 and b < 100:
                red_pixels.append((x, y))
                
    if red_pixels:
        # Calculate the bounding box of red pixels to find the player's center
        min_x = min(p[0] for p in red_pixels)
        max_x = max(p[0] for p in red_pixels)
        min_y = min(p[1] for p in red_pixels)
        max_y = max(p[1] for p in red_pixels)
        center_x = (min_x + max_x) // 2
        center_y = (min_y + max_y) // 2
        
        # In Game Boy overworld, the player character is ALWAYS centered in the middle of the screen!
        # The center of the screen is at x=80, y=72 (or tile x=4, y=4 of a 9x8 tile grid).
        # Wait, if the player is always at the center, then the screenshot center is the player.
        # But the background shifts!
        # Let's find the background coordinates from the game's RAM if we could, but we can't.
        # Instead, is there any coordinate labels drawn on the image?
        # Let's check if the image has labels. In the sandbox/ directory, we have no labeled images on disk, only clean ones.
        print(f"Red pixels found in {img_path}: {len(red_pixels)} pixels. Bounding box: ({min_x}, {min_y}) to ({max_x}, {max_y}), Center: ({center_x}, {center_y})")
    else:
        print(f"No red pixels found in {img_path}.")

find_player_sprite("screenshots/screenshot_1788093216840.png")
find_player_sprite("screenshots/screenshot_1788093259922.png")
find_player_sprite("state_current.png")
