from PIL import Image

def analyze_screenshot(filename):
    img = Image.open(filename).convert('RGB')
    img_std = img.resize((160, 144), Image.Resampling.NEAREST)
    
    # Check some pixels in the text box area (y=112 to 143)
    # Dialogue box border at y=112 (Check if solid black)
    is_border_black = all(img_std.getpixel((x, 112))[0] < 80 for x in range(10, 150))
    
    # Dialogue box background at y=122 (Check if solid cream)
    bg_colors = [img_std.getpixel((x, 122)) for x in range(20, 140)]
    avg_r = sum(c[0] for c in bg_colors) / len(bg_colors)
    avg_g = sum(c[1] for c in bg_colors) / len(bg_colors)
    avg_b = sum(c[2] for c in bg_colors) / len(bg_colors)
    
    print(f"File: {filename}")
    print(f"  Border black: {is_border_black}")
    print(f"  Avg BG color: ({avg_r:.1f}, {avg_g:.1f}, {avg_b:.1f})")

for f in ["mansion_switch_dialogue_open.png", "mansion_switch_dialogue_step2.png", "mansion_switch_dialogue_step3.png", "mansion_switch_dialogue_final.png"]:
    try:
        analyze_screenshot(f)
    except Exception as e:
        print(f"Error {f}: {e}")
