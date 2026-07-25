import mgba
import time

def main():
    print("Starting systematic warp search on B1F Platform 1...")
    # Walkable area: columns 24 to 27, rows 14 to 18
    # We are currently at (25, 15) on B1F.
    # Let's walk to (24, 14) and then snake through columns 24 to 27 and rows 14 to 18.
    
    # Simple path to cover columns 24-27, rows 14-18.
    # Start at (25, 15).
    # Walk Left to 24: "Left" (at 24, 15)
    # Walk Up to 14: "Up" (at 24, 14)
    # Now at (24, 14).
    # Let's trace a path:
    # Row 14: Right to 27 -> "Right", "Right", "Right" (reaches 27, 14)
    # Move to Row 15: "Down" (at 27, 15)
    # Row 15: Left to 24 -> "Left", "Left", "Left" (reaches 24, 15)
    # Move to Row 16: "Down" (at 24, 16)
    # Row 16: Right to 27 -> "Right", "Right", "Right" (reaches 27, 16)
    # Move to Row 17: "Down" (at 27, 17)
    # Row 17: Left to 24 -> "Left", "Left", "Left" (reaches 24, 17)
    # Move to Row 18: "Down" (at 24, 18)
    # Row 18: Right to 27 -> "Right", "Right", "Right" (reaches 27, 18)
    
    steps = [
        "Left", "Up",  # to (24, 14)
        "Right", "Right", "Right", # Row 14
        "Down",
        "Left", "Left", "Left", # Row 15
        "Down",
        "Right", "Right", "Right", # Row 16
        "Down",
        "Left", "Left", "Left", # Row 17
        "Down",
        "Right", "Right", "Right" # Row 18
    ]
    
    # We will step one-by-one and print our position.
    # If the map changes or we warp, we will notice because:
    # 1. get_coordinates() will change to a 1F coordinate or 0,0
    # 2. Or we will see the map change in screenshots.
    
    for i, move in enumerate(steps):
        mgba.press_buttons([move, "sleep 300"])
        pos = mgba.get_coordinates()
        print(f"Step {i+1}: {move} -> {pos}")
        
        # Check if coordinates look like we transitioned to 1F or B2F or if we hit a wall/battle
        if pos['x'] == 0 and pos['y'] == 0:
            time.sleep(0.5)
            pos = mgba.get_coordinates()
            print(f"Re-check: {pos}")
            
        # If we warped, let's stop
        # On 1F, our position would be around (25, 15). But let's check if the coordinates
        # are outside of columns 24-27 and rows 14-18 (which would mean we warped or are in battle)
        if not (24 <= pos['x'] <= 27 and 14 <= pos['y'] <= 18) and not (pos['x'] == 0 and pos['y'] == 0):
            print("Warp detected! Stopping search.")
            mgba.take_screenshot()
            break

if __name__ == "__main__":
    main()
